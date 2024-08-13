#!/usr/bin/env python3
"""lists all documents in a mongoDB collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in a given MongoDB collection.

    :param mongo_collection: The pymongo collection object
    :return: A list of documents
    """
    return (list(mongo_collection.find()))
