import os
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
   return "Application is Runngin!!!"

if __name__ == "__main__":
    os.system("nohup python sbi.py &")
    application.run()
