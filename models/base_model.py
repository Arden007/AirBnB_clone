#!/usr/bin/bin/python3
"""
Defines the base model class
"""
import uuid
from datetime import datetime
from .__init__ import storage


class BaseModel:
    """
    The BaseModel defines all common attributes/methods for other classes
    Also links BaseModel to FileStorage by using the variable storage
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes an instance
        """
        if kwargs is not None and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        String representation when instance is printed
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Save updates to an instance
        """
        self.__dict__.update({"update_at": datetime.now()})
        storage.save()
    
    def to_dict(self):
        """
        Returns a dict representation of an instance
        """
        disdict = dict(self.__dict__)
        disdict.update({'__class__': type(self).__name__,
                        'updated_at': self.updated_at.isoformat(),
                        'id': self.id,
                        'created_at': self.created_at.isoformat()})
        return disdict
    