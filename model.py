from flask_login import UserMixin

from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()

class Recipe(Base):
    __tablename__  = 'recipe'
    id = Column(Integer, primary_key=True)
    # ADD YOUR FIELD BELOW ID
    name_of_publisher=Column(String)
    name_of_recipe=Column(String)
    country=Column(String)
    ingredients=Column(String)
    picture=Column(String)
    how_to_make=Column(String)


# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel


class User(UserMixin, Base):
    __tablename__ = 'user'
    id            = Column(Integer, primary_key=True)
    email         = Column(String)
    pw_hash       = Column(String)
    authenticated = Column(Boolean, default=False)

    def __repr__(self):
      return "<User: %s, password: %s>" % (
        self.email, self.pw_hash)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
