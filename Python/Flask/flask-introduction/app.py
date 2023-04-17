#import flask
from flask import Flask

#setup application
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)