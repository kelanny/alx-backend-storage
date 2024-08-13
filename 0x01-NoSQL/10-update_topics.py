#!/usr/bin/env python3
"""Changes the content of mongoDB document"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on its name.

    :param mongo_collection: The pymongo collection object
    :param name: The name of the school document to update
    :param topics: A list of topics to set in the document
    :return: None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
