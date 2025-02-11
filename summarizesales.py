import json
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def summarize_sales():
    sales_data = redis_client.lrange("sales", -100, -1)
    summary = {}
    for sale_json in sales_data:
        sale = json.loads(sale_json)
        details = sale["Sale"][0]
        salesman = details["SalesMan"]
        quantity = details["WhatSold"]["quantity"]
        unit_price = details["WhatSold"]["UnitPrice"]

        if salesman not in summary:
            summary[salesman] = {"sales_count": 0, "total_quantity": 0, "total_revenue": 0}
        summary[salesman]["sales_count"] += 1
        summary[salesman]["total_quantity"] += quantity
        summary[salesman]["total_revenue"] += quantity * unit_price

    print("Summary for last 100 sales:")
    for salesman, data in summary.items():
        print(f"{salesman}: Sales: {data['sales_count']}, "
              f"Quantity: {data['total_quantity']}, "
              f"Revenue: {data['total_revenue']}")

summarize_sales()

