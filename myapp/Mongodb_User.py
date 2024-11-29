from pymongo import MongoClient
from myapp import bcrypt

class MongoUser:
    collection = None

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    @staticmethod
    def set_collection(mongodb):
        MongoUser.collection = mongodb['users']


    @staticmethod
    def validate(data):
        if "first_name" not in data or "last_name" not in data or "email" not in data or "password" not in data:
            raise ValueError("All Fields Are Required")
        return True

    def save(self):
        if MongoUser.collection is None:
            raise ValueError("Database Collection Not Set")
        if MongoUser.collection.find_one({"email": self.email}):
            raise ValueError("Email Already Exit")
        MongoUser.collection.insert_one(self.to_dict())

    def hash_password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)



