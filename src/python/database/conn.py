from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from __init__ import config_db


engine = create_engine(config_db['url'])

Session = sessionmaker(bind=engine)

session = Session()


