from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_mongoengine import MongoEngine
from models import Trending
import os
import json

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'popular'}
db = MongoEngine(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html") 

@app.route('/getJson', methods=['GET', 'POST'])
def getJson():
    trendings = Trending.query()
    for trending in trendings:
        print (trending)
    return jsonify({'ok': True})

if __name__ == '__main__':
    #os.system('python .\startSpider.py')
    app.run(debug=True)
