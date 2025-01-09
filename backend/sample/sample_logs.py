from models.log import Log

sample_logs = [
    {
        "log_id": "log124",
        "seeker_id": "9e5958a9-ce37-4427-8b69-a65c30b9fa2f",
        "classification_result": {
            "categories": ["youth", "single mothers"],
            "confidence_score": 0.92
        },
        "processing_time_ms": 450,
        "request": {"message": "I'm struggling with faith."},
        "response": {"message": "Let us guide you."},
        "timestamp": "2025-01-01T12:05:00Z"
    },
]

for log_data in sample_logs:
    log = Log(
        log_id=log_data["log_id"],
        seeker_id=log_data["seeker_id"],
        classification_result=log_data["classification_result"],
        processing_time_ms=log_data["processing_time_ms"],
        request=log_data["request"],
        response=log_data["response"],
        timestamp=log_data["timestamp"]
    )
    log.save()
