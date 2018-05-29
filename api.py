from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
users = {}

class User(Resource):

    def get (self,user_id):
        return {user_id:users[user_id]}
    def put (self, user_id):
        users[username] = request.form['data']
        return{user_id:users[user_id]}


api.add_resource(User,'/<string:user_id>')


if __name__ == '__main__':
    app.run(debug=True)
