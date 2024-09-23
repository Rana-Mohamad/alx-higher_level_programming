#!/usr/bin/python3
'''Creates city class'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''Class City'''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey="states.id", nullable=False)


class State(Base):
    '''Class state'''
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
