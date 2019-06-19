import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager

from resources.versa import Versa




app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.config["PROPAGATE_EXCEPTIONS"]=True
app.secret_key="Matteo"
api=Api(app)


jwt = JWTManager (app)


#app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=5)

app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(weeks=100)
"""
@app.before_first_request
def create_table():
    db.create_all()
"""




api.add_resource(Versa, "/versa")
#api.add_resource(Login, "/login")




if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
