#!/usr/bin/python3

""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy.orm import relationship
from sqlalchemy import Column, string, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(string(128), nullable=False)
        state_id = (string(60), Foreignkey('state.id'), nullable=False)
        places = relationship('place', backref='cities',
                              cascade='all, delete, delete-orphan')

    else:
        name = ''
        state_id = ''
