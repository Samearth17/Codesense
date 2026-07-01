from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
engine = create_engine('sqlite:///mydb.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

session = sessionmaker(bind=engine)()

#query
users = session.query(User).all() 
for user in users: 
 print(f"User: {user.name}, Email: {user.email}")