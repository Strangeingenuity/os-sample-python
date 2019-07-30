from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    response = requests.get('https://httpbin.org/ip')
    return "Hello World!"
    

if __name__ == "__main__":
    application.run()
