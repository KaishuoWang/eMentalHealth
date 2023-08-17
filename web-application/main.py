
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/train')
def train():
    return 'This is the page for user to submit training data'

@app.route("/search/<sample_query>")
def search(sample_query):
    try:
        return {'record-ids': [1,2], 'descriptions':['Your query is ' + sample_query, 'This is a sample']}
    except ValueError:
        return "invalid input"