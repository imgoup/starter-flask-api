from flask import Flask, jsonify, request
import os
import requests
from requests_html import AsyncHTMLSession

app = Flask(__name__)
asession = AsyncHTMLSession()


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route('/play', methods=['POST', 'GET'])
def getPlayUrl():
    async def getPlay():
        playload = {'url': request.form['link'], 'token': 'G7eRpMaa'}
        r = await asession.get('https://dlpanda.com', params=playload)
        data = {
            'id': 1343,
            'url': r.html.find("source", first=True).attrs["src"]
        }

        return data
    result = asession.run(getPlay,getPlay,getPlay,getPlay,getPlay,getPlay,getPlay,getPlay,getPlay,getPlay)
    print(result)
    return result
