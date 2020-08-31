from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource, reqparse
import json

APP = Flask(__name__)
API = Api(APP)


def simplemessage(string):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": string
                    }
                }
            ]
        }
    }


class timetable(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('userRequest', type=dict)
        parser.add_argument('bot', type=dict)
        args = parser.parse_args()
        user_id = args['userRequest']['user']['id']
        data = json_loader('userdata.json').load()
        if data.get(user_id) is None:
            return simplemessage('유저정보가 등록되지 않았습니다. 유저 정보를 등록해주세요.')


class food_menu(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('userRequest', type=dict)
        parser.add_argument('bot', type=dict)
        args = parser.parse_args()
        userinfo = args['userRequest']


class register(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('userRequest', type=dict)
        parser.add_argument('bot', type=dict)
        parser.add_argument('action', type=dict)
        args = parser.parse_args()
        user_id = args['userRequest']['user']['id']
        action = args['action']
        params = action['params']
        grade = params['학년']
        group = params['반']
        loader = json_loader('userdata.json')
        data = loader.load()
        result = jsonify(simplemessage(f'{grade}-{group} 으로 등록 되었습니다.')) if data.get(user_id) is None \
            else jsonify(simplemessage(f'{grade}-{group} 으로 변경 되었습니다.'))
        data[user_id] = {
            '학년': grade,
            '반': group
        }
        loader.write(data)
        return result


class json_loader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename) as json_file:
            return json.load(json_file)

    def write(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, ensure_ascii=False)


API.add_resource(register, '/register')
API.add_resource(timetable, '/timetable')
API.add_resource(food_menu, '/food_menu')

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=7000)
