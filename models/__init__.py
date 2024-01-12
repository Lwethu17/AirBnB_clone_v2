#!/usr/bin/python3
"""This module instantiates an object from class FileStorage"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique FileStorage/DBStorage instance for all the models.
"""
storage.reload()
