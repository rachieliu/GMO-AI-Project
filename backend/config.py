#config.py-- Connects to database

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



# Connect to the Database using the CONNECTION STRING (all teammates need this)
uri = "mongodb+srv://rachieliu10:gmoAIProject2024@gmocluster.b2h9x.mongodb.net/?retryWrites=true&w=majority&appName=GMOCluster"

# Create a new client and connect to the server
#Client = Instance of MongoDB aka connection
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)