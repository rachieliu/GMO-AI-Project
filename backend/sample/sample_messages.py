from models.message import Message

sample_messages = [
    {
        "seeker_id": "9e5958a9-ce37-4427-8b69-a65c30b9fa2f",  
        "content": "I have a question about faith.",
        "classification": "faith struggles",
        "language": "English",
        "timestamp": "2025-01-01T12:00:00Z"
    },
]

for message_data in sample_messages:
    message = Message(
        seeker_id=message_data["seeker_id"],
        content=message_data["content"],
        classification=message_data["classification"],
        language=message_data["language"],
        timestamp=message_data["timestamp"]
    )
    message.save()
