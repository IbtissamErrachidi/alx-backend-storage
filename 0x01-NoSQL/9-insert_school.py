#!/usr/bin/env python3
"""This module covers insertion of a document to MongoDB in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    insert into school
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
