# sample_seekers.py
from datetime import datetime

import sys
import os

# Add the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.seeker import Seeker
from models.metadata import Metadata


# Sample Seekers with metadata fields
sample_seekers = [
    {
        "contact_uuid": "9e5958a9-ce37-4427-8b69-a65c30b9fa2f",
        "first_name": "James",
        "last_name": "Davis",
        "source": "Referral",
        "language_code": "fr",
        "decision": "Interested: Seeking More Information",
        "country": "Canada",
        "region": "East Coast",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
        "metadata": [
            Metadata(type="phone_number", value="+1234567890"),  # Example of metadata
            Metadata(type="source", value="Referral")  # Example of metadata
        ]
    },
    {
        "contact_uuid": "38e17775-9913-4454-b033-048d7c3252cd",
        "first_name": "Noah",
        "last_name": "Smith",
        "source": "Referral",
        "language_code": "es",
        "decision": "Committed: Ready for Next Steps",
        "country": "Germany",
        "region": "Southern",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "f90aca22-3118-4cc8-a1f4-a7899a03e675",
        "first_name": "James",
        "last_name": "Garcia",
        "source": "Social_Media_Outreach",
        "language_code": "de",
        "decision": "Exploring: Open to Discussion",
        "country": "Canada",
        "region": "Northern",
        "state": "Texas",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "7b1df54a-687f-4157-8856-e6692f81e352",
        "first_name": "Noah",
        "last_name": "Rodriguez",
        "source": "Website_Inquiry",
        "language_code": "en",
        "decision": "Interested: Seeking More Information",
        "country": "China",
        "region": "Midwest",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "62652c75-40cf-4f32-aa49-1d7464eec497",
        "first_name": "Lucas",
        "last_name": "Williams",
        "source": "Event_Signup",
        "language_code": "es",
        "decision": "Exploring: Open to Discussion",
        "country": "China",
        "region": "East Coast",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "8d7f0a13-7fb8-4a49-ae06-31880fea35bb",
        "first_name": "Amelia",
        "last_name": "Brown",
        "source": "Email_Newsletter",
        "language_code": "es",
        "decision": "Interested: Seeking More Information",
        "country": "Germany",
        "region": "West Coast",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "77b23957-cb6a-475e-8b1f-2b4321ece8bf",
        "first_name": "Mia",
        "last_name": "Miller",
        "source": "Social_Media_Outreach",
        "language_code": "en",
        "decision": "Interested: Seeking More Information",
        "country": "Germany",
        "region": "Midwest",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "846af86a-eb46-4b9e-ae0b-6cd2ba2bf126",
        "first_name": "Lucas",
        "last_name": "Johnson",
        "source": "Email_Newsletter",
        "language_code": "en",
        "decision": "Interested: Seeking More Information",
        "country": "United States",
        "region": "East Coast",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "4a876aed-e8e1-49dd-b526-c76c35754460",
        "first_name": "Noah",
        "last_name": "Martinez",
        "source": "Referral",
        "language_code": "fr",
        "decision": "Committed: Ready for Next Steps",
        "country": "Germany",
        "region": "Midwest",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "847733aa-5a78-4ac1-85a9-7744257de671",
        "first_name": "Sophia",
        "last_name": "Smith",
        "source": "Referral",
        "language_code": "zh",
        "decision": "Interested: Seeking More Information",
        "country": "Canada",
        "region": "Midwest",
        "state": "Texas",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "1e8a4b4d-e560-4377-9836-e758be2bb8c9",
        "first_name": "Lucas",
        "last_name": "Rodriguez",
        "source": "Website_Inquiry",
        "language_code": "zh",
        "decision": "Committed: Ready for Next Steps",
        "country": "China",
        "region": "Midwest",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "4ef55322-58da-4c6d-924f-cd2930b25f24",
        "first_name": "Mia",
        "last_name": "Williams",
        "source": "Event_Signup",
        "language_code": "es",
        "decision": "Exploring: Open to Discussion",
        "country": "United States",
        "region": "Midwest",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "7f5acbb1-35ee-42e0-80d5-671f9876cef5",
        "first_name": "Ethan",
        "last_name": "Miller",
        "source": "Website_Inquiry",
        "language_code": "de",
        "decision": "Interested: Seeking More Information",
        "country": "United States",
        "region": "Northern",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "524a5bd3-ddc3-47fb-9ce9-a4b2d50afcd8",
        "first_name": "Olivia",
        "last_name": "Davis",
        "source": "Social_Media_Outreach",
        "language_code": "es",
        "decision": "Interested: Seeking More Information",
        "country": "Germany",
        "region": "Southern",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "62d21ec0-12c5-4174-9b19-b772e77d90c5",
        "first_name": "Lucas",
        "last_name": "Davis",
        "source": "Website_Inquiry",
        "language_code": "fr",
        "decision": "Committed: Ready for Next Steps",
        "country": "China",
        "region": "East Coast",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "52fc5809-995b-472b-bd20-209f3edc3891",
        "first_name": "James",
        "last_name": "Miller",
        "source": "Event_Signup",
        "language_code": "fr",
        "decision": "Interested: Seeking More Information",
        "country": "United States",
        "region": "West Coast",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "d5e4bb70-01e7-4d54-a786-3d33aed6167e",
        "first_name": "Noah",
        "last_name": "Smith",
        "source": "Website_Inquiry",
        "language_code": "zh",
        "decision": "Committed: Ready for Next Steps",
        "country": "Spain",
        "region": "Southern",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "2db691b4-d82c-4faf-bc96-bd5657da441a",
        "first_name": "Mia",
        "last_name": "Johnson",
        "source": "Social_Media_Outreach",
        "language_code": "en",
        "decision": "Interested: Seeking More Information",
        "country": "United States",
        "region": "Southern",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "da127c28-fdcb-465e-8248-8729ce8a4f18",
        "first_name": "Isabella",
        "last_name": "Miller",
        "source": "Website_Inquiry",
        "language_code": "es",
        "decision": "Committed: Ready for Next Steps",
        "country": "Spain",
        "region": "East Coast",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "d0c68907-2971-44d1-a6af-7fab17acc58a",
        "first_name": "Isabella",
        "last_name": "Smith",
        "source": "Referral",
        "language_code": "en",
        "decision": "Interested: Seeking More Information",
        "country": "Spain",
        "region": "Northern",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "ea1fe850-7dd0-4f22-8dff-8fad74ab614d",
        "first_name": "Ethan",
        "last_name": "Williams",
        "source": "Social_Media_Outreach",
        "language_code": "de",
        "decision": "Committed: Ready for Next Steps",
        "country": "Canada",
        "region": "Midwest",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "893e5b9b-ce95-48e2-a5fa-da0a49b7786c",
        "first_name": "Isabella",
        "last_name": "Rodriguez",
        "source": "Email_Newsletter",
        "language_code": "fr",
        "decision": "Interested: Seeking More Information",
        "country": "Spain",
        "region": "Northern",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "2f3db8d5-2866-4eb6-ab49-50ea78345750",
        "first_name": "Ethan",
        "last_name": "Davis",
        "source": "Social_Media_Outreach",
        "language_code": "en",
        "decision": "Committed: Ready for Next Steps",
        "country": "Germany",
        "region": "Southern",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "6d51bccf-1b49-4ab4-9b85-af74686282c0",
        "first_name": "Alexander",
        "last_name": "Martinez",
        "source": "Social_Media_Outreach",
        "language_code": "de",
        "decision": "Interested: Seeking More Information",
        "country": "Spain",
        "region": "West Coast",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "d3ba0004-79f5-4775-a17a-df088c08cac0",
        "first_name": "Lucas",
        "last_name": "Johnson",
        "source": "Referral",
        "language_code": "de",
        "decision": "Exploring: Open to Discussion",
        "country": "United States",
        "region": "East Coast",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "31432149-0745-4cb9-97a4-e311dd40c9f3",
        "first_name": "Mia",
        "last_name": "Miller",
        "source": "Event_Signup",
        "language_code": "en",
        "decision": "Interested: Seeking More Information",
        "country": "China",
        "region": "Southern",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "c6e1dcbe-9966-40f9-904f-d205e6c664e8",
        "first_name": "Mia",
        "last_name": "Brown",
        "source": "Email_Newsletter",
        "language_code": "fr",
        "decision": "Exploring: Open to Discussion",
        "country": "Spain",
        "region": "West Coast",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "0100e016-4420-4904-92dd-d9c316043be4",
        "first_name": "Sophia",
        "last_name": "Brown",
        "source": "Social_Media_Outreach",
        "language_code": "de",
        "decision": "Committed: Ready for Next Steps",
        "country": "Canada",
        "region": "Midwest",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "890835f6-a175-4125-8cf8-19d625a34505",
        "first_name": "Isabella",
        "last_name": "Martinez",
        "source": "Event_Signup",
        "language_code": "en",
        "decision": "Exploring: Open to Discussion",
        "country": "China",
        "region": "East Coast",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "1998e26d-407e-4dc6-8e19-dce5265e76f2",
        "first_name": "Mia",
        "last_name": "Garcia",
        "source": "Referral",
        "language_code": "fr",
        "decision": "Committed: Ready for Next Steps",
        "country": "Canada",
        "region": "Southern",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "04408398-5139-4825-8333-c06e5d06dc65",
        "first_name": "Noah",
        "last_name": "Brown",
        "source": "Website_Inquiry",
        "language_code": "fr",
        "decision": "Exploring: Open to Discussion",
        "country": "China",
        "region": "East Coast",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "9109bc86-b40d-44f9-922d-7bca36c5cb3d",
        "first_name": "Mia",
        "last_name": "Williams",
        "source": "Event_Signup",
        "language_code": "zh",
        "decision": "Interested: Seeking More Information",
        "country": "United States",
        "region": "Southern",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "e42b03bb-b47d-4866-89aa-e96508f76731",
        "first_name": "Mia",
        "last_name": "Smith",
        "source": "Event_Signup",
        "language_code": "fr",
        "decision": "Interested: Seeking More Information",
        "country": "China",
        "region": "Midwest",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "841d7c9a-9c24-4532-a380-3f2e17ebca1b",
        "first_name": "Sophia",
        "last_name": "Smith",
        "source": "Social_Media_Outreach",
        "language_code": "en",
        "decision": "Committed: Ready for Next Steps",
        "country": "United States",
        "region": "Midwest",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "2431e622-53b3-40ea-bb41-3a4171fddff2",
        "first_name": "Noah",
        "last_name": "Johnson",
        "source": "Website_Inquiry",
        "language_code": "fr",
        "decision": "Interested: Seeking More Information",
        "country": "Canada",
        "region": "West Coast",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "21d882e0-22fe-4e5d-a808-8232c6936eae",
        "first_name": "Noah",
        "last_name": "Rodriguez",
        "source": "Email_Newsletter",
        "language_code": "en",
        "decision": "Exploring: Open to Discussion",
        "country": "United States",
        "region": "Northern",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "47a0901b-e5d8-478a-bd7c-e98ecc59b27d",
        "first_name": "James",
        "last_name": "Garcia",
        "source": "Event_Signup",
        "language_code": "de",
        "decision": "Interested: Seeking More Information",
        "country": "United States",
        "region": "Southern",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "2cacd2c8-23b9-4534-90a1-39b711011fe8",
        "first_name": "James",
        "last_name": "Johnson",
        "source": "Email_Newsletter",
        "language_code": "en",
        "decision": "Interested: Seeking More Information",
        "country": "Germany",
        "region": "Northern",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "d7c5d9e2-5979-41a8-be96-f20c121b9052",
        "first_name": "James",
        "last_name": "Davis",
        "source": "Referral",
        "language_code": "de",
        "decision": "Interested: Seeking More Information",
        "country": "Spain",
        "region": "Northern",
        "state": "New York",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "3f1e92c9-7e16-45d9-82f5-735ae8894282",
        "first_name": "Noah",
        "last_name": "Miller",
        "source": "Social_Media_Outreach",
        "language_code": "es",
        "decision": "Exploring: Open to Discussion",
        "country": "United States",
        "region": "West Coast",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "90cb60ed-9130-451f-8a1a-3d590caec3d1",
        "first_name": "Amelia",
        "last_name": "Rodriguez",
        "source": "Website_Inquiry",
        "language_code": "fr",
        "decision": "Interested: Seeking More Information",
        "country": "United States",
        "region": "Southern",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "0d214bdb-5149-4f33-928d-ffc08b7e0066",
        "first_name": "Alexander",
        "last_name": "Johnson",
        "source": "Referral",
        "language_code": "en",
        "decision": "Committed: Ready for Next Steps",
        "country": "United States",
        "region": "Northern",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "021a54a8-b2a7-434d-82c8-872d9dcefd87",
        "first_name": "Sophia",
        "last_name": "Davis",
        "source": "Event_Signup",
        "language_code": "en",
        "decision": "Committed: Ready for Next Steps",
        "country": "United States",
        "region": "West Coast",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "219b20ec-e099-4a52-b3ab-1b6a2203602a",
        "first_name": "Ethan",
        "last_name": "Smith",
        "source": "Event_Signup",
        "language_code": "en",
        "decision": "Committed: Ready for Next Steps",
        "country": "Spain",
        "region": "West Coast",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "e892d9fb-7905-4ac6-a10e-fe5d2a24bdf8",
        "first_name": "Mia",
        "last_name": "Smith",
        "source": "Referral",
        "language_code": "es",
        "decision": "Exploring: Open to Discussion",
        "country": "United States",
        "region": "Southern",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "f81e729f-f50a-46a3-adda-7a6d16872881",
        "first_name": "Isabella",
        "last_name": "Martinez",
        "source": "Social_Media_Outreach",
        "language_code": "de",
        "decision": "Interested: Seeking More Information",
        "country": "Canada",
        "region": "Southern",
        "state": "Illinois",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "f65913c4-38bc-46c2-8486-074bdecb370a",
        "first_name": "Amelia",
        "last_name": "Davis",
        "source": "Social_Media_Outreach",
        "language_code": "es",
        "decision": "Exploring: Open to Discussion",
        "country": "China",
        "region": "West Coast",
        "state": "Florida",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "e84dbb41-6cb7-44c4-a0d5-a324e0beb075",
        "first_name": "James",
        "last_name": "Brown",
        "source": "Website_Inquiry",
        "language_code": "zh",
        "decision": "Interested: Seeking More Information",
        "country": "Canada",
        "region": "Southern",
        "state": "Texas",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "3a760f48-2048-4af3-bd89-11c4cc03d435",
        "first_name": "Noah",
        "last_name": "Davis",
        "source": "Referral",
        "language_code": "en",
        "decision": "Exploring: Open to Discussion",
        "country": "China",
        "region": "Northern",
        "state": "Texas",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    },
    {
        "contact_uuid": "bfc3b09b-8ab5-49f1-bb41-271275c38fb2",
        "first_name": "Noah",
        "last_name": "Brown",
        "source": "Event_Signup",
        "language_code": "en",
        "decision": "Exploring: Open to Discussion",
        "country": "United States",
        "region": "Southern",
        "state": "California",
        "messages": [
            {
                "type": "Contact",
                "message": "Hello, I am interested in learning more about your organization."
            },
            {
                "type": "OM",
                "message": "Thank you for reaching out! Could you share more about what you're looking for?"
            }
        ],
         "metadata": []
    }
]
# Delete all existing seekers in the database
from backend.config import client
db = client["gospel_seeker_connection"]
seekers_collection = db["seekers"]
match_logs_collection = db["match_logs"]  # New collection for storing message logs
seekers_collection.delete_many({})  # This deletes all documents in the "seekers" collection

# Insert each new seeker into the database
for seeker_data in sample_seekers:
    # Create an instance of Seeker for each entry in sample_seekers
    seeker = Seeker(
        name=f"{seeker_data['first_name']} {seeker_data['last_name']}",
        contact_info={
            "contact_uuid": seeker_data["contact_uuid"],
            "language_code": seeker_data["language_code"]
        },
        messages=seeker_data["messages"],
        metadata=seeker_data["metadata"]
    )

    # Save the Seeker object to the database
    seeker.save()  # Save seeker

    # Log each message as a match log (between Seeker and OM)
    for message in seeker_data["messages"]:
        if message["type"] == "OM":  # Only log OM responses as match logs
            match_log = {
                "seeker_contact_uuid": seeker_data["contact_uuid"],
                "message_type": message["type"],
                "message_content": message["message"],
                "timestamp": datetime.utcnow()  # Timestamp for when the interaction occurred
            }
            match_logs_collection.insert_one(match_log)  # Insert match log into match_logs collection