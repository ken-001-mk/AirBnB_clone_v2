#!/usr/bin/python3

""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from model.city import City

STORAGE = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if STORAGE == 'db':
	name = Column(String(128), nullable=False)
	cities = relationship('city', backref='states', 
			     cascade='all', delete-orphan)

    else:
	name = ''
	@property
	def cities(Self):
	    from models import storage
	    list_city = []
	    all_ins = storage.all(City)
	    for value in all_ins.values()
		if value.state_id == self.id:
		    list_city.append(value)
	    return list_city
