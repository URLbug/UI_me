from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):

  __tablename__ = 'user'

  user_id = Column(Integer, primary_key=True)
  first_name = Column(String(40))
  last_name = Column(String(50))
  email = Column(String(100))
  password = Column(String(100))


