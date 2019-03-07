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
    return render_template('home2.html')

@app.route('/company_all')
def companyAll():
    allData = db['company_profile'].find({})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']
       
        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories

        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_name')
def Company_name():
    Company_name = request.args.get('name')
    allData = db['company_profile'].find({'Company_name': {'$regex': Company_name,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_address')
def Company_address():
    Company_address = request.args.get('address')
    allData = db['company_profile'].find({'Company_address': {'$regex': Company_address,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_descriptions')
def Company_descriptions():
    Company_descriptions = request.args.get('desc')
    allData = db['company_profile'].find({'Company_descriptions': {'$regex': Company_descriptions,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_email')
def Company_email():
    Company_email = request.args.get('email')
    allData = db['company_profile'].find({'Company_email': {'$regex': Company_email,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_phone')
def Company_phone():
    Company_phone = request.args.get('phone')
    allData = db['company_profile'].find({'Company_phone': {'$regex': Company_phone,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_fax')
def Company_fax():
    Company_fax = request.args.get('fax')
    allData = db['company_profile'].find({'Company_fax': {'$regex': Company_fax,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_web')
def Company_web():
    Company_web = request.args.get('web')
    allData = db['company_profile'].find({'Company_web': {'$regex': Company_web,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_maps')
def Company_maps():
    Company_maps = request.args.get('maps')
    allData = db['company_profile'].find({'Company_maps': {'$regex': Company_maps,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_products')
def Company_products():
    Company_products = request.args.get('products')
    allData = db['company_profile'].find({'Company_products_and_services': {'$regex': Company_products,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

@app.route('/company_categories')
def Company_categories():
    Company_categories = request.args.get('categories')
    allData = db['company_profile'].find({'Company_categories': {'$regex': Company_categories,'$options': 'i'}})
    dataJson = []
    for data in allData:
        id = data['_id']
        Company_name = data['Company_name']
        Company_address = data['Company_address']
        Company_descriptions = data['Company_descriptions']
        Company_email = data['Company_email']
        Company_phone = data['Company_phone']
        Company_fax = data['Company_fax']
        Company_web = data['Company_web']
        Company_maps = data['Company_maps']
        Company_products = data['Company_products_and_services']
        Company_categories = data['Company_categories']

        dataDict = {
            'id': str(id),
            'Company_name': Company_name,
            'Company_address' : Company_address,
            'Company_descriptions' : Company_descriptions,
            'Company_email' : Company_email,
            'Company_phone' : Company_phone,
            'Company_fax' : Company_fax,
            'Company_web' : Company_web,
            'Company_maps' : Company_maps,
            'Company_products' :Company_products,
            'Company_categories' : Company_categories
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

if __name__ == '__main__':
    app.debug = True
    app.run()