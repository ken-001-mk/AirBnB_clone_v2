#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declaractive_base
from models import storage_type

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60),
                nullable=False,
                primary_key=True,
                unique=True)

    created_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())

    updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k in kwargs:
		if k in ['created_at', 'updated_at']:
		    setattr(self, k, datetime.fromisoformat(kwargs[k]))
		elif k != '__class__':
		    setattr(self, k, kwargs[k])
	    if storage_type = 'db':
		if not hasattr(self, 'id'):
		    setattr(self, id, str(uuid4()))

		if not hasattr(kwargs, 'created_at'):
		    setattr(self, 'created_at', datetime.now())

		if not hasattr(kwargs, 'updated_at'):
		    setattr(self, , 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
    self._class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
	storage.save(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
	dictionary['__class__'] = self.__class__.__name__
	for k in dictionary:
	    if type(dictionary[k] is datetime:
		dictionarary[k].isoformat()

	if '_sa_instance_state' in dictionary.keys():
	    del (dictionary['_sa_instance_state'])
        return dictionary

    def delete(self):
	"""delete the current instance from storage"""
	from models import storage
	storage.delete(self)
