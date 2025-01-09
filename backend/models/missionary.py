# models/missionary.py
from backend.config import client  
from bson import ObjectId

class Missionary:
    def __init__(self, name, phone_number, email, expertise, languages_spoken, location, availability, preferred_metadata=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.expertise = expertise
        self.languages_spoken = languages_spoken
        self.location = location
        self.availability = availability
        self.preferred_metadata = preferred_metadata or []

    # Save the missionary to MongoDB
    def save(self):
        db = client["gospel_seeker_connection"]  
        missionaries_collection = db["missionaries"] 

        # Check if the missionary already exists by their email (can change to something else)
        existing_missionary = missionaries_collection.find_one({"email": self.email})

        if existing_missionary:
            print(f"Missionary with email {self.email} already exists. Skipping insert.")
            return existing_missionary["_id"]  # Return the existing missionary's _id
        else:
            # If no duplicate exists, insert the new missionary document
            result = missionaries_collection.insert_one(self.__dict__)  # Insert the object as a document
            print(f"Missionary {self.name} inserted successfully.")
            return result.inserted_id  # Return the inserted document's ID

    # Get all missionaries
    @staticmethod
    def get_all():
        db = client["gospel_seeker_connection"]
        missionaries_collection = db["missionaries"]
        return missionaries_collection.find()

    # Find a missionary by ID
    @staticmethod
    def find_by_id(missionary_id):
        db = client["gospel_seeker_connection"]
        missionaries_collection = db["missionaries"]
        return missionaries_collection.find_one({"_id": ObjectId(missionary_id)})

    # Method to update an existing missionary document
    def update(self, missionary_id):
        db = client["gospel_seeker_connection"]
        missionaries_collection = db["missionaries"]
        result = missionaries_collection.update_one(
            {"_id": ObjectId(missionary_id)}, {"$set": self.__dict__}
        )
        return result.modified_count

    # Delete a missionary document
    def delete(self, missionary_id):
        db = client["gospel_seeker_connection"]
        missionaries_collection = db["missionaries"]
        result = missionaries_collection.delete_one({"_id": ObjectId(missionary_id)})
        return result.deleted_count
