from flask import Flask, jsonify
from flask_cors import CORS
import urllib.request
import json

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/movies/<movie>', methods=['GET'])
def movies(movie):
    response_object = {'status': 'success'}
    print(movie)
    contents = urllib.request.urlopen("http://www.omdbapi.com/?s="+movie+"&apikey=101cdcd1").read()
    contents = json.loads(contents.decode('utf-8'))
    contents = contents['Search']
    return jsonify(contents)

if __name__ == '__main__':
    app.run()