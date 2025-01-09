from backend.config import client
from bson import ObjectId  # Import ObjectId to store MongoDB document IDs

class Metadata:
    def __init__(self, type, value, seeker_id=None):
        self.type = type
        self.value = value
        self.seeker_id = seeker_id  # Reference to the associated Seeker (optional)

    def save(self):
        db = client["gospel_seeker_connection"]
        metadata_collection = db["metadata"]
        result = metadata_collection.insert_one(self.__dict__)  # Insert the metadata document
        return result.inserted_id  # Return the inserted document's ID

    @staticmethod
    def get_all():
        db = client["gospel_seeker_connection"]
        metadata_collection = db["metadata"]
        return metadata_collection.find()

    @staticmethod
    def find_by_id(metadata_id):
        db = client["gospel_seeker_connection"]
        metadata_collection = db["metadata"]
        return metadata_collection.find_one({"_id": ObjectId(metadata_id)})
