import os
import time
import re
from slackclient import SlackClient
import requests
from bs4 import BeautifulSoup
#from flask import Flask

#application = Flask(__name__)

EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
RTM_READ_DELAY = 1
slack_client = SlackClient(os.environ.get('SLACKBOT_API_TOKEN'))
starterbot_id = None

@application.route("/")
def handle_command():
    """
         Executes bot command if the command is known
    """
    if slack_client.rtm_connect(with_team_state=False,auto_reconnect=True):
        print("Starter Bot connected and running!!!!!!")
        print("Hey Guys !!! Hello OpenShift!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read(), starterbot_id)
            if command:
                # Default response is help text for the user
                default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

                # Finds and executes the given command, filling in response
                response = None
                # This is where you start to implement more commands!
                response = requests.get("https://kumiai.remit.co.jp/exchange/")
                response.encoding = response.apparent_encoding
                bs = BeautifulSoup(response.text, 'html.parser')

                if command.startswith(EXAMPLE_COMMAND):
                    for tr in bs.select('table.rate_table')[0].select('tr'):
                        if tr.select('th')[0].text == 'Myanmar':
                            # value = '\n\n{} : {} => {}\n'.format(tr.select('th')[0].text,tr.select('td')[0].text,tr.select('td')[1].text)
                            # response = "Sure...write some more code then I can do that!"
                            response = '\n\n{} : {} => {}\n'.format(tr.select('th')[0].text,tr.select('td')[0].text,tr.select('td')[1].text)

                # Sends the response back to the channel
                slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text=response or default_response
                )
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")

def parse_bot_commands(slack_events, starterbot_id):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

if __name__ == "__main__":
    print("starting app...")
    #handle_command()
    #application.run()
