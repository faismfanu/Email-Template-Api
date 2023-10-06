#Imported Packages
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from pymongo import MongoClient

#Configure Flask & JWT
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a secure secret key
jwt = JWTManager(app)

#MongoDB connection
client = MongoClient("mongodb+srv://faism904841:Faism9048@cluster0.aqi8f3d.mongodb.net/?retryWrites=true&w=majority")
db = client["flask_template_manager"]

#User registration