# models/category.py
from backend.config import client

class Category:
    def __init__(self, name, description, path_type, related_languages, expertise_required):
        self.name = name
        self.description = description
        self.path_type = path_type
        self.related_languages = related_languages
        self.expertise_required = expertise_required

    def save(self):
        db = client["gospel_seeker_connection"]
        categories_collection = db["categories"]
        result = categories_collection.insert_one(self.__dict__)
        print(f"Category {self.name} inserted successfully.")
        return result.inserted_id

    @staticmethod
    def get_all():
        db = client["gospel_seeker_connection"]
        categories_collection = db["categories"]
        return categories_collection.find()
