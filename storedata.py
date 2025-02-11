import json
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

sales = {
    "Sale": [
        {
            "SalesMan": "Jenny",
            "CustomerName": {
                "title": "Mr",
                "first": "Alexander",
                "last": "Hart"
            },
            "CustomerAddress": {
                "street": {
                    "number": 3603,
                    "name": "Henry Street"
                },
                "city": "Helsinki",
                "state": "Uusimaa",
                "country": "Finland",
                "postcode": "0088",
                "coordinates": {
                    "latitude": "-3.7209",
                    "longitude": "-141.2083"
                }
            },
            "WhatSold": {
                "Product": "Keyboard",
                "quantity": 5000,
                "UnitPrice": 200
            },
            "email": "alexander.hart@example.com",
            "age": 35,
            "DateOfBirth": "29-Feb-1990",
            "phone": "071-989-0175",
            "cell": "081-064-9679"
        }
    ]
}


redis_client.rpush("sales", json.dumps(sales))