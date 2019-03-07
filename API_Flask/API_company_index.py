from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import yaml

app = Flask(__name__)
config = yaml.load(open('database.yaml'))
client = MongoClient(config['uri'])
# db = client.dbSgMaritime
db = client['dbSgMaritime']
CORS(app)

@app.route('/')
def index():
    return render_template('home1.html')

@app.route('/company_all')
def companyAll():
    allData = db['company_index'].find({})
    dataJson = []
    for data in allData:
        id = data['_id']
        comname = data['company_name']
        url = data['url_name']
        date = data['crawled_on']
        dataDict = {
            'id': str(id),
            'name': comname,
            'url': url,
            'crawl_date' : date
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_name')
def company_name():
    compname = request.args.get('name')
    allData = db['company_index'].find({'company_name': {'$regex': compname,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        comname = data['company_name']
        url = data['url_name']
        date = data['crawled_on']
        dataDict = {
            'id': str(id),
            'name': comname,
            'url': url,
            'crawl_date' : date
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)



@app.route('/url_name')
def url_name():
    url_name = request.args.get('url')
    allData = db['company_index'].find({'url_name': {'$regex': url_name,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        comname = data['company_name']
        url = data['url_name']
        date = data['crawled_on']
        dataDict = {
            'id': str(id),
            'name': comname,
            'url': url,
            'crawl_date' : date
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/crawled_on')
def crawled_on():
    crawled_on = request.args.get('crawled')
    allData = db['company_index'].find({'crawled_on': {'$regex': crawled_on,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        comname = data['company_name']
        url = data['url_name']
        date = data['crawled_on']
        dataDict = {
            'id': str(id),
            'name': comname,
            'url': url,
            'crawl_date' : date
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

if __name__ == '__main__':
    app.debug = True
    app.run()