#!/usr/bin/env python3
""" Inserts a new document in a mongodb collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the collection with the given attributes.

    :param mongo_collection: The pymongo collection object
    :param kwargs: Key-value pairs to be used as the document's fields
    :return: The _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return (result.inserted_id)
