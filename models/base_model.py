#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel():

    id = Column(
        String(60),
        nullable=False,
        primary_key=True,
        unique=True
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    # tODO ''' __iNiT__ method '''
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:  # ? is not impty
            for key, value in kwargs.items(): # ? loop in the dict

                    if hasattr(self, key) == True: # ? if the key is in the dict
                        self.__dict__[key] = value
                        setattr(self, key, value) # ? set the key with the value

    # tODO ''' SAVE method '''

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        #!"""!!!!! passing the self it great aidea !!!!!"""
        storage.new(self)
        storage.save()

    # tODO '''TO_DICT method'''

    # def to_dict(self):
    #     my_dict_z = {}
    #     x = self.updated_at.isoformat()
    #     y = self.created_at.isoformat()

    #     lk = self.__dict__

    #     for k, v in lk.items():
    #         if k == "updated_at":
    #             my_dict_z["__class__"] = self.__class__.__name__
    #             my_dict_z[k] = x
    #             continue
    #         elif k == "created_at":
    #             my_dict_z[k] = y
    #         else:
    #             my_dict_z[k] = v

    #     return my_dict_z
    
    def to_dict(self):
        state_dict = self.__dict__.copy()
        state_dict.pop('_sa_instance_state', None)
        return state_dict

    # tODO ''' __STR__ method return string when print the object '''

    def __str__(self):

        clase_name = self.__class__.__name__
        id_us = self.id
        dictn = str(self.__dict__)

        rus_z = "[{:s}] ({:s}) {:s}".format(clase_name, id_us, dictn)

        return rus_z
    
    def delete(self):
        from models import storage
        storage.delete(self)

    #! xxxxxxxxxxxxxxxxxxxx


# self *z
