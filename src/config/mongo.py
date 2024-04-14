from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.checkin_checkout_db

employees_collection = db.employees
records_collection = db.records