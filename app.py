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
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400'}
    r = requests.get('https://dlpanda.com/?url=https%3A%2F%2Fv.douyin.com%2FiJGmPD6y%2F&token=G7eRpMaa', headers=headers)
    return f'{r.status_code}{r.content}'
    
    
