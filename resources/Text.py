from flask import request
from flask_restful import Resource
from common import utils

class InputText(Resource):
    def post(self):
        input = request.get_json()
        # diacritized_text = utils.diacritize(input)
        # return diacritized_text
        split_text = utils.splitStringToArray(input['text'])
        print(split_text)
        return split_text

    def transliterate(self, text):
        pass
