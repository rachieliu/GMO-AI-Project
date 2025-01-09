from pymongo import MongoClient

# Connect to MongoDB Atlas using the connection string
client = MongoClient("mongodb+srv://rachieliu10:gmoAIProject2024@gmocluster.b2h9x.mongodb.net/?retryWrites=true&w=majority")

# Connect to the database
db = client["gospel_seeker_connection"]

def clear_all_data():
    # Get a list of all collections in the database
    collections = db.list_collection_names()

    for collection in collections:
        # For each collection, drop all documents
        print(f"Clearing data from collection: {collection}")
        db[collection].delete_many({})

    print("All data cleared from all collections.")

# Call the function to clear all data
clear_all_data()
