import json
from flask import Flask, jsonify, make_response, request, Response

app = Flask(__name__)

class GetAPI:
    def __init__(self):
        self.name = name
    @app.route("/aws/<name>",methods=["GET"])
    def get_json(self,name):
        try:
            NAME = self.name
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
      
