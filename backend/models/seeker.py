# models/seeker.py
from backend.config import client  # Absolute import for client
from bson import ObjectId  # To store documents in binary form (ObjectId)

class Seeker:
    # Constructor method called when a new Seeker is created
    def __init__(self, name, contact_info, messages=None, metadata=None):
        self.name = name
        self.contact_info = contact_info
        self.messages = messages or []
        self.metadata = metadata or []

        # Automatically assign a 'contact_uuid' as the MongoDB ObjectId
        self.contact_info['contact_uuid'] = str(ObjectId())  # Use a new ObjectId for contact_uuid

    # Insert a new Seeker document into the Seekers collection
    def save(self):
        db = client["gospel_seeker_connection"]
        seekers_collection = db["seekers"]

        # Ensure  'contact_uuid' field exists before saving
        contact_uuid = self.contact_info.get('contact_uuid')
        if not contact_uuid:
            print("contact_uuid is required to save a seeker.")
            return None

        # Check if a Seeker with the same contact_uuid already exists
        existing_seeker = seekers_collection.find_one({"contact_uuid": contact_uuid})
        if existing_seeker:
            # If the Seeker already exists, print a message and return the existing Seeker's _id
            print(f"Seeker with contact_uuid {contact_uuid} already exists. Skipping insert.")
            return existing_seeker["_id"]
        else:
            # Save the metadata if available
            if self.metadata:
                metadata_ids = []
                for metadata_obj in self.metadata:
                    metadata_id = metadata_obj.save()  # Save the metadata object and get the ObjectId
                    metadata_ids.append(metadata_id)
                self.metadata = metadata_ids  # Store the metadata ObjectIds in the Seeker document

            # Insert the new Seeker document into the database
            result = seekers_collection.insert_one({
                'name': self.name,
                'contact_info': self.contact_info,
                'messages': self.messages,
                'metadata': self.metadata
            })
            print(f"Seeker {contact_uuid} inserted successfully.")
            return result.inserted_id  # Return the inserted document's ID

    # Fetch all seekers
    @staticmethod
    def get_all():
        db = client["gospel_seeker_connection"]
        seekers_collection = db["seekers"]
        return seekers_collection.find()

    # Find a Seeker by unique id
    @staticmethod
    def find_by_id(seeker_id):
        db = client["gospel_seeker_connection"]
        seekers_collection = db["seekers"]
        return seekers_collection.find_one({"_id": ObjectId(seeker_id)})

    # Update an existing Seeker document in the collection
    def update(self, seeker_id):
        db = client["gospel_seeker_connection"]
        seekers_collection = db["seekers"]
        result = seekers_collection.update_one(
            {"_id": ObjectId(seeker_id)}, {"$set": self.__dict__}
        )
        return result.modified_count

    # Delete a Seeker document from the collection based on Seeker ID
    def delete(self, seeker_id):
        db = client["gospel_seeker_connection"]
        seekers_collection = db["seekers"]
        result = seekers_collection.delete_one({"_id": ObjectId(seeker_id)})
        return result.deleted_count
