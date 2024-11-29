from flask import Flask
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from pymongo import MongoClient


app = Flask(__name__)
# username = "IkhiloyaO"
# password = "Ikhis@2024!!"
#
# encoded_username = quote_plus(username)
# encoded_password = quote_plus(password)


app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = "8900dkioeFNFNFNnsnbjdvjdjd74757"
# uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.jyy5h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# url = "mongodb+srv://IkhiloyaO:Ikhis%402024!!@cluster0.jyy5h.mongodb.net/patient_data?retryWrites=true&w=majority"
#
# client = MongoClient(uri)
#
# mongodb = client['patient_data']

db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from myapp import routes
# from myapp.Mongodb_User import MongoUser
# from myapp.Mongodb_Patients import MongoPatients
# MongoUser.set_collection(mongodb)
# MongoPatients.set_collection(mongodb)
