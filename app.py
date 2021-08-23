from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from resources.Text import InputText

app = Flask(__name__)
api = Api(app)
CORS(app)

# routes
api.add_resource(InputText, "/transliterate")



if __name__ == "__main__":
    app.run(debug=True, port=5001)
