from datatest.models.Base import Base
from datatest.models.Pet import Pet
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    pets = relationship(Pet)
