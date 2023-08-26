from flask import Flask, jsonify, request
import os
import requests
from requests_html import HTMLSession

app = Flask(__name__)
session = HTMLSession()


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route('/play', methods=['POST', 'GET'])
def getPlayUrl():
    playload = {'url': request.form['link'], 'token': 'G7eRpMaa'}
    r = session.get('https://dlpanda.com', params=playload)
    data = {
        'id': 1343,
        'url': r.html.find("source", first=True).attrs["src"]
    }
    return jsonify(data)
