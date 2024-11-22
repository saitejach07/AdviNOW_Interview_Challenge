from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Business(Base):
    __tablename__ = 'businesses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    symptoms = relationship("Symptom", back_populates="business")


class Symptom(Base):
    __tablename__ = 'symptoms'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    diagnostic = Column(String, nullable=True)
    business_id = Column(Integer, ForeignKey("businesses.id")) #1 to many 

    business = relationship("Business", back_populates="symptoms")
