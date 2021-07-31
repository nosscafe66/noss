# coding:utf-8
import json
from flask import Flask, jsonify, make_response, request, Response

app = Flask(__name__)

class PostAPI:
    def __init__(self):
        pass
    @app.route('/aws', methods=['POST'])
    def post_json(self):
        try:
            json = request.get_json() #get POST JSON
            NAME = json["name"]
            result = {
              "data":{
                "id":1
                ,"name":NAME
              }
            }
            return jsonify(result)
        except Exception as erromessage:
            print(erromessage)
if __name__ == "__main__":
    app.run()
