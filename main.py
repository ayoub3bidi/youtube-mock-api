from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="View of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

names = {'tim': {'age': 19, 'gender': 'male' },'bill': {'age': 24 , 'gender': 'male' }}

# class HelloWorld(Resource):
#     def get(self, name):
#         return names[name]

#     def post(self):
#         return {'data': 'posted'}

# api.add_resource(HelloWorld, '/hello/<string:name>')

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}

api.add_resource(Video, '/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)