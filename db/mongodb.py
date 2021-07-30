from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Loading the database

password = os.environ["mongopassword"]
mongo_url = "mongodb+srv://pw1924:" + password + "@appdb.ao3yl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = MongoClient(mongo_url)
db = cluster["WSV"]

# Collections

punishments = db["punishments"]
settings = db["settings"]
