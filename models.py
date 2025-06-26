from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, nullable=False)
    dateofbirth = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
