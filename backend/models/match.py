#models/models.py
#Collection to store seeker- missionary matches

from backend.config import client
from bson import ObjectId
from datetime import datetime 

class Match:
    def __init__(self, seeker_id, missionary_id, match_score, match_reason, status="active"):
       
        self.seeker_id = seeker_id
        self.missionary_id = missionary_id
        self.match_score = match_score
        self.match_reason = match_reason
        self.status = status
        self.match_date = datetime.datetime.utcnow()  # Date when the match was created
        self.last_updated = self.match_date  # Initially set to match_date

    def save(self):
        
        db = client["gospel_seeker_connection"]
        matches_collection = db["matches"]
        
        # Insert the match document into the collection
        result = matches_collection.insert_one(self.__dict__)
        print(f"Match between Seeker {self.seeker_id} and Missionary {self.missionary_id} inserted successfully.")
        return result.inserted_id  # Return the inserted document ID

    @staticmethod
    def get_by_seeker(seeker_id):
        
        #Retrieve all matches for a specific seeker.
        db = client["gospel_seeker_connection"]
        matches_collection = db["matches"]
        return matches_collection.find({"seeker_id": ObjectId(seeker_id)})

    @staticmethod
    def get_by_missionary(missionary_id):
        
       #Retrieve all matches for a specific missionary.
        db = client["gospel_seeker_connection"]
        matches_collection = db["matches"]
        return matches_collection.find({"missionary_id": ObjectId(missionary_id)})

    @staticmethod
    def get_all():
       
        #Retrieve all matches from the collection.
        db = client["gospel_seeker_connection"]
        matches_collection = db["matches"]
        return matches_collection.find()
