from flask import Flask, jsonify
from flask_cors import CORS
import urllib, urllib.parse
import json
import requests
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/movies/name/<movie>', methods=['GET'])
def movies(movie):
    movie = urllib.parse.quote(movie)
    search = cache.get(movie)
    if search != None:
        return jsonify(search)
    contents = urllib.request.urlopen("http://www.omdbapi.com/?s="+movie+"&apikey=101cdcd1").read()
    contents = json.loads(contents.decode('utf-8'))
    contents = contents['Search']
    cache.set(movie, contents)
    return jsonify(contents)

@app.route('/movies/id/<id>', methods=['GET'])
def movie(id):
    search = cache.get(id)
    if search != None:
        return jsonify(search)
    contents = urllib.request.urlopen("http://www.omdbapi.com/?i="+id+"&apikey=101cdcd1&plot=full").read()
    contents = json.loads(contents.decode('utf-8'))
    cache.set(id, contents)
    return jsonify(contents)

@app.route('/movies/trailer/<name>', methods=['GET'])
def trailer(name):
    name = name + " Trailer HD"
    name = urllib.parse.quote(name)
    search = cache.get(name)
    if search != None:
        return jsonify(search)
    contents = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/search?key=AIzaSyB_Wp8ZT8yb-qtouEc9lwOAur3Lx6meRmw&part=snippet&maxResults=1&q=" + name).read()
    contents = json.loads(contents.decode('utf-8'))
    cache.set(name, contents)
    return jsonify(contents)

if __name__ == '__main__':
    app.run()