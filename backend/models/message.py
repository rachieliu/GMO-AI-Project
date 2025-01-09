# models/message.py
# Message Collection: To record of all messages exchanged between the seeker and the system

from backend.config import client  # Import the database client to connect to MongoDB
from bson import ObjectId  # Import ObjectId to handle MongoDB's unique document IDs
from datetime import datetime  # Import datetime to get the current timestamp for each message

class Message:
    def __init__(self, seeker_id, message, language, category_match, matched_missionary_id, ai_response=None):
        #Initialize the Message object.
        
        self.seeker_id = seeker_id  # The ID of the seeker
        self.message = message  # The content of the message
        self.timestamp = datetime.utcnow()  # Store the timestamp of when the message is created
        self.language = language  # Detected language of the message ("en", "fr")
        self.category_match = category_match  # Category of the message ("Crisis", "Relationships")
        self.matched_missionary_id = matched_missionary_id  # ID of the missionary matched based on the message
        self.type = "Seeker"  # Default type is Seeker for the initial message
        self.ai_response = ai_response  # The AI-generated response to the seeker. Default is none

    def save(self):
        
        db = client["gospel_seeker_connection"]  # Connect to the database
        messages_collection = db["messages"]  # Specify the `messages` collection
        
        # Insert the message document into MongoDB
        result = messages_collection.insert_one(self.__dict__)  # Insert the document based on the current instance's attributes
        print(f"Message inserted for Seeker {self.seeker_id} successfully.")  # Output to confirm insertion
        return result.inserted_id  # Return the inserted document's ID

    @staticmethod
    def get_all():
       #Retrieve all messages from message collection
        db = client["gospel_seeker_connection"]  # Connect to the database
        messages_collection = db["messages"]  
        return messages_collection.find()  # Return all documents in the collection

    @staticmethod
    def find_by_id(message_id):
        # Find and return the document by its ObjectId
        
        db = client["gospel_seeker_connection"]  
        messages_collection = db["messages"]  
        return messages_collection.find_one({"_id": ObjectId(message_id)})  

    def update(self, message_id):
        #Update an existing message document with new info
        db = client["gospel_seeker_connection"] 
        messages_collection = db["messages"]  
        result = messages_collection.update_one(
            {"_id": ObjectId(message_id)}, {"$set": self.__dict__}  
        )
        return result.modified_count  # Return the number of modified documents

    def delete(self, message_id):
       # Delete  message by its ObjectId
        db = client["gospel_seeker_connection"] 
        messages_collection = db["messages"] 
        result = messages_collection.delete_one({"_id": ObjectId(message_id)})  
        return result.deleted_count  # Return the number of deleted documents
