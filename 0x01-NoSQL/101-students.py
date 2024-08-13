#!/usr/bin/env python3
# 101-students.py
""" Queries mongoDB collection with python"""


def top_students(mongo_collection):
    """
    Returns a list of students sorted by their average score.

    Parameters:
    mongo_collection: The pymongo collection object for the students.

    Returns:
    list: A list of dictionaries, each containing a student's name and av score
          sorted by av score in desc order. Each dict has the following keys:
          - '_id': The student's unique identifier.
          - 'name': The student's name.
          - 'averageScore': The student's av score across all topics.
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    return (list(mongo_collection.aggregate(pipeline)))
