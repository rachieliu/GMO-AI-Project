from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle CORS
from backend.models.seeker import Seeker  # Import Seeker model
from backend.models.missionary import Missionary  # Import Missionary model (you can implement this later)
from backend.models.message import Message  # Import Message model (you can implement this later)
from datetime import datetime
import json  # Import for pretty printing the received data

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Route to handle POST requests from the frontend form
@app.route('/submit-conversation', methods=['POST'])
def submit_conversation():
    data = request.get_json()

    # Log the received data (for debugging)
    if data:
        print("Received data:", json.dumps(data, indent=4)) 
    else:
        print("No data received")

    # Extract information from the form data
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    decision = data.get('decision')
    contact_value_phone = data.get('contactValuePhone')
    contact_value_email = data.get('contactValueEmail')
    text_input = data.get('textInput')

    # Handle the conversation (mock handling for now)
    # Later will do: Classify text, detect language, match missionary 
    seeker = Seeker(
        name=f"{first_name} {last_name}",
        contact_info={"phone": contact_value_phone, "email": contact_value_email},
        messages=[{"message": text_input, "type": "Seeker", "timestamp": datetime.utcnow()}]
    )

    # Save the Seeker to the database
    seeker_id = seeker.save()  

    # Example response (will be replaced with actual classification/ matching stuff later)
    result = {
        "analysis": "This is a mock response for testing",  # AI-generated response placeholder
        "language": "en",  # Language detected 
        "region": "US",  #  region 
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Running on port 5001
