from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    role = Column(String)
    # ADD THIS LINE IF MISSING:
    balance = Column(Float, default=0.0)

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    location = Column(String)
    price = Column(Float)
    tour_url = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

class Inquiry(Base):
    """ Represents a 'Demand' reaching out to a 'Supply' """
    __tablename__ = "inquiries"
    id = Column(Integer, primary_key=True, index=True)
    demand_id = Column(Integer, ForeignKey("users.id"))
    property_id = Column(Integer, ForeignKey("properties.id"))
    
    # Relationship to get student balance easily
    student = relationship("User") 
    property = relationship("Property")