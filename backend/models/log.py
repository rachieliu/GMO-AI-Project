# models/log.py
# for storing logs of actions, errors

from backend.config import client  # Import the database client to connect to MongoDB
from bson import ObjectId  # Import ObjectId to handle MongoDB's unique document IDs
from datetime import datetime  # Import datetime to get the current timestamp for each log

class Log:
    def __init__(self, log_type, message, source, severity_level, data=None):
      
        self.log_type = log_type
        self.timestamp = datetime.utcnow()  # Store the timestamp of when the log is created
        self.message = message
        self.source = source
        self.severity_level = severity_level
        self.data = data or {}

    def save(self):
       
        db = client["gospel_seeker_connection"]  # Connect to the database
        logs_collection = db["logs"]  # Specify the `logs` collection
        
        # Insert the log document into MongoDB
        result = logs_collection.insert_one(self.__dict__)  # Insert the document based on the current instance's attributes
        print(f"Log inserted: {self.message}")  # Output to confirm insertion
        return result.inserted_id  # Return the inserted document's ID

    @staticmethod
    def get_all():
        db = client["gospel_seeker_connection"]  # Connect to the database
        logs_collection = db["logs"]  # Specify the `logs` collection
        return logs_collection.find()  # Return all documents in the collection

    @staticmethod
    def find_by_id(log_id):
        db = client["gospel_seeker_connection"] 
        logs_collection = db["logs"] 
        return logs_collection.find_one({"_id": ObjectId(log_id)})  # Find and return the document by  ObjectId

    def update(self, log_id):
        db = client["gospel_seeker_connection"]  
        logs_collection = db["logs"] 
        result = logs_collection.update_one(
            {"_id": ObjectId(log_id)}, {"$set": self.__dict__}  # Update the log document with the new data
        )
        return result.modified_count  # Return the number of modified documents

    def delete(self, log_id):
        
        db = client["gospel_seeker_connection"] 
        logs_collection = db["logs"]  
        result = logs_collection.delete_one({"_id": ObjectId(log_id)})  # Delete the log by its ObjectId
        return result.deleted_count  # Return the number of deleted documents
