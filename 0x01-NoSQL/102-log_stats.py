#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.

The script will output:
- The total number of logs.
- The count of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
- The number of logs where the method is GET and the path is /status.
- The top 10 most present IPs in the logs, sorted by their count.
"""

from pymongo import MongoClient


def log_stats():
    """Function that prints stats about Nginx logs in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count of logs with method=GET and path=/status
    status_check_count = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print(f"{status_check_count} status check")

    # Top 10 most present IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_collection.aggregate(pipeline)

    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
