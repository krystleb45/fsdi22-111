from flask import Flask  # from the flask model impport the Flask class.

app = Flask(__name__)  # We are instantiating our Flask class into
# our app vairable.


@app.route("/")                 # A decorator that creats a new HTTP path
def index():                    # In the context of flask, this is a view function
    return "<h1> Hello, World!<h1>"  # return statement


@app.route("/users/krystle")
def about_krystle():

    me = {
        "first_name": "Krystle",
        "laste_name": "Berry",
        "hobbies": "Woodworking"
    }
    return me
# my strong = "Hello, %s %s !" % (first_name, last_name)


@app.route("/greeting/<name>")
def print_name(name):
    return "<h1>Hello, %s!</h1>" % name


@app.route("/square/<int:num>")
def square_num(num):
    return "<h1> That number, squared, is: %s</h1>" % (num**2)
