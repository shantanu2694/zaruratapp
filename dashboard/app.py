from flask import Flask
from flask_restful import Api
from dashboard import Dashboard


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'shantanu'
api = Api(app)



api.add_resource(Dashboard, '/dashboard')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # important to mention debug=True