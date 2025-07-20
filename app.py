
from flask import Flask

app = Flask(__name__)

@app.route("/") # connet the specific web page into specific function 
def home():
    return "hello user! this is my fist flask app"

@app.route("/about")
def about():
    return 'this is about page'

@app.route("/contant")
def contant():
    return "this is contant us page"


if __name__ == "__main__":
    app.run(debug=True)