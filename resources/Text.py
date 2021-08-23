from flask import request
from flask_restful import Resource

class InputText(Resource):
    def post(self):
        data = request.get_json()
        uppercase = data['text'].upper()
        return uppercase

    def transliterate(self, text):
        pass
