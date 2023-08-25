from flask import Flask
import os
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
@app.route('/play/<link>')
def getPlayUrl(link):
    return requests.get("https://dlpanda.com/?url=https%3A%2F%2Fv.douyin.com%2FiJGmPD6y%2F&token=G7eRpMaa").content
    
    
