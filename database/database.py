
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

uri = os.getenv("uri")


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'),tls=True, tlsCAFile=certifi.where())

db = client["questions_db"]
mcq_collection = db["mcq_collection"]
tf_collection = db["tf_collection"]
fill_collection = db["fill_collection"]
formula_collection = db["formula_collection"]





#trash

# formula_collection = db["formula_collection"]

# print(client.list_database_names())

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

