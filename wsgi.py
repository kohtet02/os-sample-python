from flask import Flask
import sbi

application = Flask(__name__)

@application.route("/")
def hello():
    return "Application is running!!"

if __name__ == "__main__":
    app = sbi()
    app.run()
    #application.run()
