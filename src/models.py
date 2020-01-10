import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(50), nullable=False)

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    profile_picture = Column(String(250), nullable=False)
    biography = Column(String(250))
    follower_count = Column(Integer)
    following_count = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    comments = Column(String(250))
    likes = Column(Integer)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))
    
class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    comments = Column(String(250))

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comments = Column(String(250))
    reply = Column(String(250))

class DirectMessage(Base):
    __tablename__ = 'direct message'
    id = Column(Integer, primary_key=True)
    search = Column(String(250))
    conversation = Column(String)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')