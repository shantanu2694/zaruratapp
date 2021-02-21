from flask import Flask
from flask_restful import Api
from cart import CartGet
from cart import CartDelete
from cart import CartAdd


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'shantanu'
api = Api(app)


api.add_resource(CartGet, '/cart')
api.add_resource(CartAdd, '/cart/add')
api.add_resource(CartDelete, '/cart/delete')

if __name__ == '__main__':
    app.run(debug=True, port=5002)  #  to mention debug=True