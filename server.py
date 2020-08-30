from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource, reqparse
from comcigan import School
import json

APP = Flask(__name__)
API = Api(APP)


class timetable(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('userRequest', type=dict)
        parser.add_argument('bot', type=dict)
        args = parser.parse_args()
        userinfo = args['userRequest']
        botinfo = args['bot']


class carte(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('userRequest', type=dict)
        parser.add_argument('bot', type=dict)
        args = parser.parse_args()
        userinfo = args['userRequest']
        botinfo = args['bot']


class register(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('userRequest', type=dict)
        parser.add_argument('bot', type=dict)
        args = parser.parse_args()
        userinfo = args['userRequest']
        botinfo = args['bot']

class skill_payload(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('userRequest', type=dict)
        parser.add_argument('bot', type=dict)
        parser.add_argument('action', type=dict)
        args = parser.parse_args()
        action = args['action']
        user_id = args['userRequest']['user']['id']
        # 파라미터 가져오기
        loader = json_loader('userdata.json')
        user_data = loader.load()
        user_data[user_id] # 가져온 파라미터로 지정

class json_loader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename) as json_file:
            return json.load(json_file)

    def write(self, data):
        with open(self.filename) as file:
            json.dump(data, file)

