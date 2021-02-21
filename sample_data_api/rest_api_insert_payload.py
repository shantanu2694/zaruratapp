import json
import pymongo
from flask import Flask
from flask import request



app = Flask(__name__)
client = pymongo.MongoClient("mongodb://dev:dev@localhost:27017/eassy_connection")
database = client['eassy_connection']
collection = database['SampleCollection']


@app.route("/sampledata", methods=['POST'])
def insert_document():
    req_data = request.get_json()
    collection.insert_one(req_data).inserted_id
    return ('', 204)


@app.route('/sampledata')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)


if __name__ == '__main__':
    app.run()
