from flask import Flask
application = Flask(__name__)
import requests

@application.route("/")
def hello():
    response = requests.get('https://httpbin.org/ip')
    return response
    

if __name__ == "__main__":
    application.run()
