#!/usr/bin/python3
"""State module for HolbertonBnB project"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    """Represents the amenity data set"""
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
