import subprocess
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
   return "Application is Runngin!!!"

if __name__ == "__main__":
    subprocess.Popen("nohup python sbi.py &", shell=True)
    application.run()
