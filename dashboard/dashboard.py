from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from mongo_connection import database_access



class Dashboard(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('product_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    parser.add_argument('price',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self):
        database = database_access()
        collection = database['dashboard']
        records = collection.find()
        services = []
        for record in records:
            if record['count'] is not 0:
                services.append({'product_name': record['product_name'], 'price': record['price'], 'messege': 'stock is avaliable'})
                return {'dashboard': services}
            else:
                return {'messege': 'no product is avaliable !!'}


    @jwt_required()
    def post(self):
        database = database_access()
        collection = database['dashboard']
        data = Dashboard.parser.parse_args()
        query = {"product_name": data['product_name'], "price": data['price']}
        records = collection.insert(query)
        database.close()
        return {"message": "Row inserted successfully."}, 201
