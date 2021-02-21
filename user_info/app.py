from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from logger import configure_logger
from dashboard import Dashboard

logging = configure_logger('handlers', 'logs/app.log')
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'zarurat'
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(Dashboard, '/dashboard')

if __name__ == '__main__':
    app.run(debug=True)

