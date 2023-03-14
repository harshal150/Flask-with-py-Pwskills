from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!1</h1>"

@app.route("/harshhh")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/sushant")
def hello_world3():
    return "<h1>Hello, World!3</h1>"

@app.route("/bhavesh")
def hello_world4():
    return "<h1>Hello, World!4</h1>"

@app.route("/test2")
def testing():
    data = request.args.get('x')
    return "<h1>this is data input {} </h1>".format(data)
#https://gray-intern-ruzws.pwskills.app:5000/test2?x=harsh     url to run this method

if __name__=="__main__":
    app.run(host="0.0.0.0")
