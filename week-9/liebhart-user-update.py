# Title: liebhart-update-user.py
# Author: Nathaniel Liebhart
# Date: December 15, 2019
# Description: Exercise 9.3 - Updating and Deleting Documents
from pymongo import MongoClient
import pprint
import datetime

# Connect to local mongoDB instance and web335 database
client = MongoClient('localhost', 27017)
db = client.web335

# Update users email address
db.users.update_one(
    {"employee_id": "0000008"},
    {
        "$set": {
            "email": "cdebussy001@my365.bellevue.edu"
        }
    }
)
# Find user and output email, employee_id, first_name and last_name
pprint.pprint(db.users.find_one(
    {"employee_id": "0000008"}, {"_id": 0, "date_created": 0}))
