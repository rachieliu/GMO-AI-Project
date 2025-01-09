# sample_missionaries.py
import sys
import os

# Add the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.missionary import Missionary
sample_missionaries = [
    {
        "name": "John Doe",
        "phone_number": "+1234567890",
        "email": "john.doe@example.com",
        "expertise": ["Crisis Counseling", "Family Support", "Spiritual Guidance"],
        "languages_spoken": ["English", "Spanish"],
        "location": "USA",
        "availability": ["Monday", "Wednesday"],
        "preferred_metadata": []
    },
    {
        "name": "Jane Smith",
        "phone_number": "+0987654321",
        "email": "jane.smith@example.com",
        "expertise": ["Addiction Recovery Support", "Mental Health Counseling"],
        "languages_spoken": ["English", "French"],
        "location": "Canada",
        "availability": ["Tuesday", "Thursday", "Saturday"],
        "preferred_metadata": []
    },
    {
        "name": "David Johnson",
        "phone_number": "+1122334455",
        "email": "david.johnson@example.com",
        "expertise": ["Marriage Counseling", "Relationship Counseling"],
        "languages_spoken": ["English", "German"],
        "location": "Germany",
        "availability": ["Monday", "Friday"],
        "preferred_metadata": []
    },
    {
        "name": "Maria Garcia",
        "phone_number": "+1222333444",
        "email": "maria.garcia@example.com",
        "expertise": ["Spiritual Guidance", "Youth Counseling"],
        "languages_spoken": ["Spanish", "English"],
        "location": "Mexico",
        "availability": ["Tuesday", "Thursday"],
        "preferred_metadata": []
    },
    {
        "name": "Ethan Miller",
        "phone_number": "+1555222333",
        "email": "ethan.miller@example.com",
        "expertise": ["Crisis Counseling", "Suicide Prevention"],
        "languages_spoken": ["English", "French", "Italian"],
        "location": "UK",
        "availability": ["Monday", "Wednesday", "Friday"],
        "preferred_metadata": []
    },
    {
        "name": "Sophia Lee",
        "phone_number": "+1777888999",
        "email": "sophia.lee@example.com",
        "expertise": ["Family Support", "Crisis Counseling"],
        "languages_spoken": ["English", "Chinese"],
        "location": "China",
        "availability": ["Monday", "Thursday"],
        "preferred_metadata": []
    },
    {
        "name": "Lucas Brown",
        "phone_number": "+1888999000",
        "email": "lucas.brown@example.com",
        "expertise": ["Addiction Recovery Support", "Spiritual Guidance"],
        "languages_spoken": ["English", "Portuguese"],
        "location": "Brazil",
        "availability": ["Wednesday", "Saturday"],
        "preferred_metadata": []
    },
    {
        "name": "Olivia Harris",
        "phone_number": "+1444555666",
        "email": "olivia.harris@example.com",
        "expertise": ["Mental Health Counseling", "Crisis Counseling"],
        "languages_spoken": ["English", "Arabic"],
        "location": "UAE",
        "availability": ["Tuesday", "Friday"],
        "preferred_metadata": []
    }
]

# Save the missionaries to the database
for missionary_data in sample_missionaries:
    missionary = Missionary(**missionary_data)
    missionary.save()

print("Sample missionaries have been inserted into the database.")
