from flask import Flask, request
from flask_restful import Resource, Api
from utils import *
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class FormatAndPostMessage(Resource):

    def post(self):

        try:
            message = request.get_json()
            data = parseData(message)
            postToInfluxDB(data)
            return 200
        
        except Exception as e:
            print(e)
            return 400
        
    def get(self):

        return 200
        

api.add_resource(FormatAndPostMessage, '/')

if __name__ == '__main__':
    app.run()
