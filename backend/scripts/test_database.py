from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://rachieliu10:gmoAIProject2024@gmocluster.b2h9x.mongodb.net/?retryWrites=true&w=majority&appName=GMOCluster")  # Update with your connection string
db = client["gospel_seeker_connection"]
seekers_collection = db["seekers"]

def test_seeker_messages_and_logs(seeker_id):
    # Retrieve the Seeker document using contact_uuid inside contact_info
    seeker = seekers_collection.find_one({"contact_info.contact_uuid": seeker_id})
    
    # Check the document structure by printing it
    print("Seeker Document:", seeker)
    
    if seeker:
        print(f"Found Seeker with contact_uuid {seeker_id}")
        
        # Print specific fields if they exist
        contact_uuid = seeker.get("contact_info", {}).get("contact_uuid")
        if contact_uuid:
            print("Contact UUID:", contact_uuid)
        else:
            print("Contact UUID not found")
        
        # Print messages and metadata
        messages = seeker.get("messages", [])
        if messages:
            print("Messages:", messages)
        else:
            print("No messages found")

        metadata = seeker.get("metadata", [])
        if metadata:
            print("Metadata:", metadata)
        else:
            print("No metadata found")

    else:
        print(f"Seeker with contact_uuid {seeker_id} not found.")

# Test with a specific contact_uuid
test_seeker_messages_and_logs("9e5958a9-ce37-4427-8b69-a65c30b9fa2f")
