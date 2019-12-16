# Title: liebhart-user-service.py
# Author: Nathaniel Liebhart
# Date: December 15, 2019
# Description: Exercise 9.2 - Querying and Creating Documents
from pymongo import MongoClient
import pprint
import datetime

# Connect to local mongo instance and web335 database
client = MongoClient('localhost', 27017)
db = client.web335

# Create a new User document
user = {
    "first_name": "Claude",
    "last_name": "Debussy",
    "email": "cdebussy@me.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
}
# Insert the new User document
user_id = db.users.insert_one(user).inserted_id
# Output auto-generated user_id
print(user_id)
# Query the Users collection
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))
