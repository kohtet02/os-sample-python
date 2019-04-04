from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
   return "Application is Runngin!!!"

if __name__ == "__main__":
    print("hello")
    exec(open('sbi.py').read())
    print("its me")
    application.run()
