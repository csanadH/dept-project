from flask import Flask, jsonify, request
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

omdbapi = 'http://www.omdbapi.com/'
ytapi = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyB_Wp8ZT8yb-qtouEc9lwOAur3Lx6meRmw&"

@app.route('/movies/name', methods=['GET'])
def movies():
    movie = request.args.get('name')
    movie = urllib.parse.quote(movie)
    search = cache.get(movie)
    if search != None:
        return jsonify(search)
    contents = urllib.request.urlopen(omdbapi + "?s=" + movie + "&apikey=101cdcd1").read()
    contents = json.loads(contents.decode('utf-8'))
    contents = contents['Search']
    cache.set(movie, contents)
    return jsonify(contents)

@app.route('/movies/id', methods=['GET'])
def movie():
    id = request.args.get('movieId')
    search = cache.get(id)
    if search != None:
        return jsonify(search)
    contents = urllib.request.urlopen(omdbapi + "?i=" + id + "&apikey=101cdcd1&plot=full").read()
    contents = json.loads(contents.decode('utf-8'))
    cache.set(id, contents)
    return jsonify(contents)

@app.route('/movies/trailer', methods=['GET'])
def trailer():
    name = fetchTrailer(request.args)
    search = cache.get(name)
    if search != None:
        return jsonify(search)
    contents = urllib.request.urlopen(ytapi + "part=snippet&maxResults=1&q=" + name).read()
    contents = json.loads(contents.decode('utf-8'))
    cache.set(name, contents)
    return jsonify(contents)

def fetchTrailer(args):
    title = args.get('title')
    year = args.get('year')
    trailer = "Trailer HD"
    name = [title, year, trailer]
    name = " ".join(name)
    name = urllib.parse.quote(name)
    return name

if __name__ == '__main__':
    app.run()