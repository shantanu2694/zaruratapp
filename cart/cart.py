from flask_restful import Resource, reqparse
from mongo_connection import database_access



class CartGet(Resource):
    
    def get(self):
        database = database_access()
        collection = database['cart']
        records = collection.find()
        services = []
        for record in records:
            services.append({'product_name': record['product_name'], 'price': record['price']})
            return {'dashboard': services}


class CartAdd(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('product_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    def post(self):

        data = CartAdd.parser.parse_args()
        database = database_access()
        collection = database['dashboard']
        collcart = database['cart']
        records = collection.find(data)
        if records:
            for record in records:
                if record['count'] is not 0:
                    item = {'product_name': record['product_name'], 'price': record['price'], 'count': record['count']}
                    count = int(record['count']) - 1
                    collcart.insert(item)
                    collection.update_one(record, {"$set": {"count": count}})
                    return {'messege' : 'product has been added to cart'}
                else:
                    return {'messege': "out of stock!!!"}

class CartDelete(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('product_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    def delete(self):
        data = CartDelete.parser.parse_args()
        database = database_access()
        collcart = database['cart']
        records = collcart.find(data)
        print(records)
        if records:
            for record in records:
                collcart.remove(record)
                return {'messege': "product is removed from cart"}



