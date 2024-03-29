from flask import Flask
app=Flask(__name__)

def style_decorator(function):
    def wrapper_function():
        text=function()
        return f'<h1><b><em><u>{text}</u></em></b><h1>'
    return wrapper_function

@app.route('/')
@style_decorator
def hello_world():
    return ("Hello World")

@app.route("/shreya")
def shreya():
    return ("IM SMART")

@app.route("/nostalgia")
def nostalgia():
    return("Its a beautiful day to be alive!")

@app.route("/<name>")
def hello(name):
    return f"HI {name}"+12

if __name__=='__main__':
    app.run(debug=True)