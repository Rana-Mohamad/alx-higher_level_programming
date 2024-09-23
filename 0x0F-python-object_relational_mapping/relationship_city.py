#!/usr/bin/python3
'''Creates city class'''
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    '''Class City'''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
