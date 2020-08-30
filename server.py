from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource, reqparse
from comcigan import School

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
