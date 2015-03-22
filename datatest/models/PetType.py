from datatest.models.Base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class PetType(Base):
    __tablename__ = 'pet_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), unique=True)