from sqlalchemy import Column, ForeignKey, Integer, String
from datatest.models.Base import Base
from datatest.models.Person import Person
from datatest.models.PetType import PetType
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class Pet(Base):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey('person.id'))
    type = ForeignKey('pet_type.id')