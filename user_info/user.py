from flask_restful import Resource, reqparse
from db_connection import database_access
import yaml
import os
from logger import configure_logger


my_path = os.path.abspath(os.path.dirname(__file__))
file = yaml.safe_load(open(os.path.join(my_path, "config\\" + "application_properties.yaml")))
logging = configure_logger('default', 'logs/app.log')
db_table = file['db_table']

class User():

    TABLE_NAME = db_table
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        logging.info("finding user from datastore")
        connection = database_access()
        cursor = connection.cursor()
        query = 'SELECT * FROM {table} WHERE username=%s'.format(table=cls.TABLE_NAME)
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            logging.info("user found, returning info")
            user = cls(*row)
        else:
            logging.error("user not found, please register")
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        logging.info("finding bu user's id from datastore")
        connection = database_access()
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE id=%s".format(table=cls.TABLE_NAME)
        cursor.execute(query, (_id,))
        row = cursor.fetchone()
        if row:
            logging.info("id found, returning info")
            user = cls(*row)
        else:
            logging.error("id not found, please register")
            user = None
        connection.close()
        return user


class UserRegister(Resource):
    TABLE_NAME = db_table
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            logging.error("User with that username already exists")
            return {"message": "User with that username already exists."}, 400
        connection = database_access()
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES (NULL,%s, %s)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['username'], data['password']))
        logging.info("inserting username: {} and password: {}".format(data['username'], data['password']))
        connection.commit()
        connection.close()
        logging.info("User created successfully")
        return {"message": "User created successfully."}, 201
