from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required #JWT to  work with our app

from secure import authenticate, identity

app = Flask(__name__)
app.secret_key='just'
api = Api(app)
jwt = JWT(app, authenticate, identity) # JWT creates new end point /auth

items=[]

# c,con=connection()

class Student(Resource):
    @jwt_required()
    def get(self,name):
        for item in items:
            if item['name']==name:
                return item
            else:
                return ("not found")

    
    def post(self,name):
        data=request.get_json()
        item={'name':name,'price':data['price']}
        items.append(item)
        return item

class itemlist(Resource):
    def get(self):
        return {'Items':items}


api.add_resource(Student,'/item/<string:name>')
api.add_resource(itemlist,'/items')

app.run(port=5001, debug=True)