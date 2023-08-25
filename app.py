from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
