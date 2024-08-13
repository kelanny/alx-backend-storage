#!/usr/bin/env python3
"""returns the list of mongoDB documents that match criteria"""


def schools_by_topic(mongo_collection, topic):
    """
    Find schools that have a specific topic.

    :param mongo_collection: The pymongo collection object
    :param topic: The topic to search for
    :return: A list of documents (schools) that contain the topic
    """
    return (list(mongo_collection.find({"topics": topic})))
