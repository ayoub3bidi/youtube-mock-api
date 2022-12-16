from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
        'tim': {'age': 19, 'gender': 'male' },
        'bill': {'age': 24 , 'gender': 'male' }
        }

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {'data': 'posted'}

api.add_resource(HelloWorld, '/hello/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)