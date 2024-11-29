from pymongo import MongoClient
from myapp import bcrypt


class MongoPatients:
    collection = None

    def __init__(self, first_name, last_name, email, middle_name, phone_number,address,gender, age,
                 hypertension, ever_married, work_type, residence_type, avg_glucose_level,bmi, smoking_status, stroke):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.middle_name = middle_name
        self.phone_number = phone_number
        self.address = address
        self.gender = gender
        self.age = age
        self.hypertension = hypertension
        self.ever_married = ever_married
        self.work_type = work_type
        self.residence_type = residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.smoking_status = smoking_status
        self.stroke = stroke

    @staticmethod
    def set_collection(mongodb):
        MongoPatients.collection = mongodb["patients"]

    @staticmethod
    def validate(data):
        required_fields = ["first_name","last_name", "email", "middle_name", "phone_number","address","gender", "age",
                           "hypertension", "ever_married", "work_type", "residence_type", "avg_glucose_level","bmi", "smoking_status", "stroke"]
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"{field} is required")
        return True


    def save(self):
        if MongoPatients.collection is None:
            raise ValueError("Database Collection is not set")
        MongoPatients.collection.insert_one(self.to_dict())

    @staticmethod
    def get_all():
        return list(MongoPatients.collection.find({},{"_id":0}))

    @staticmethod
    def get_by_name(first_name):
        return MongoPatients.collection.find_one({"first_name": first_name},{"_id":0})

    @staticmethod
    def delete_name(first_name):
        return MongoPatients.collection.delete_one({"first_name": first_name})

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'phone_number': self.phone_number,
            'address': self.address,
            'gender': self.gender,
            'age': self.age,
            'hypertension': self.hypertension,
            'ever_married': self.ever_married,
            'work_type': self.work_type,
            'residence_type': self.residence_type,
            'avg_glucose_level': self.avg_glucose_level,
            'bmi': self.bmi,
            'smoking_status': self.smoking_status,
            'stroke': self.stroke
        }



