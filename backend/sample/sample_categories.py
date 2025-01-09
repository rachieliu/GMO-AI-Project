import sys
import os

# Add the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.category import Category

categories = [
    {
        "name": "General-en",
        "description": "General category for English Seekers",
        "path_type": "General",
        "related_languages": ["en"],
        "expertise_required": []  # no specific expertise
    },
    {
        "name": "Family and Marriage",
        "description": "Specialty category for family and marriage",
        "path_type": "Specialty",
        "related_languages": ["en", "es"],
        "expertise_required": ["Family Support", "Relationship Counseling"]
    },
    {
        "name": "Crisis",
        "description": "Specialty category for crisis situations",
        "path_type": "Specialty",
        "related_languages": ["en", "fr", "es"],
        "expertise_required": ["Crisis Counseling"]
    },
    {
        "name": "Spiritual Warfare",
        "description": "Specialty category for spiritual warfare",
        "path_type": "Specialty",
        "related_languages": ["en", "de"],
        "expertise_required": ["Spiritual Guidance"]
    },
    {
        "name": "Alcoholism and Drug Addiction",
        "description": "Specialty category for substance abuse issues",
        "path_type": "Specialty",
        "related_languages": ["en", "es"],
        "expertise_required": ["Addiction Recovery Support"]
    },
    {
        "name": "Suicide",
        "description": "Specialty category for suicide prevention",
        "path_type": "Specialty",
        "related_languages": ["en", "es", "fr"],
        "expertise_required": ["Suicide Prevention Counseling"]
    }
]

for category_data in categories:
    category = Category(
        name=category_data["name"],
        description=category_data["description"],
        path_type=category_data["path_type"],
        related_languages=category_data["related_languages"],
        expertise_required=category_data["expertise_required"]
    )
    category.save()
