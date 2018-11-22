from flask import Flask, jsonify
from flask_cors import CORS
import urllib.request
import json

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/movies/name/<movie>', methods=['GET'])
def movies(movie):
    contents = urllib.request.urlopen("http://www.omdbapi.com/?s="+movie+"&apikey=101cdcd1").read()
    contents = json.loads(contents.decode('utf-8'))
    contents = contents['Search']
    return jsonify(contents)

@app.route('/movies/id/<id>', methods=['GET'])
def movie(id):
    contents = urllib.request.urlopen("http://www.omdbapi.com/?i="+id+"&apikey=101cdcd1").read()
    contents = json.loads(contents.decode('utf-8'))
    return jsonify(contents)

if __name__ == '__main__':
    app.run()