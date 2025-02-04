GET /api/requests/
Response:
[
    {
        "id": 1,
        "service_type": "battery",
        "location": {
            "latitude": 9.5915,
            "longitude": 76.5222
        },
        "description": "Car tire punctured near exit 45",
        "status": "Pending",
        "created_at": "2025-02-04T14:17:14.126959Z"
    }
]

POST /api/requests/
body:
{
    "service_type": "battery",
    "location": {
        "latitude": 9.5915, 
        "longitude": 76.5222
    },
    "description": "Car tire punctured near exit 45"
}

GET 
{
    "id": 1,
    "service_type": "battery",
    "location": {
        "latitude": 9.5915,
        "longitude": 76.5222
    },
    "description": "Car tire punctured near exit 45",
    "status": "Pending",
    "created_at": "2025-02-04T14:17:14.126959Z"
}

