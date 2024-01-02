from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False)
    UserFullName = Column(String, nullable=False)
    DateStart = Column(DateTime, nullable=False)
    Status = Column(String, nullable=False)
    
