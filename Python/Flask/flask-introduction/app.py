#import flask
from flask import Flask, render_template, url_for

#setup application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

if __name__ == "__main__":
    app.run(debug=True)