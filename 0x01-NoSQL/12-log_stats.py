#!/usr/bin/env python3
"""
12-log_stats.py
Provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def print_log_stats(mongo_collection):
    # Total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count documents by HTTP methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count documents with method GET and path /status
    status_check_count = mongo_collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    print_log_stats(collection)
