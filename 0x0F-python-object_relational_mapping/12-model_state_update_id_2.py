#!/usr/bin/python3
'''
changes the name of a State object from the database hbtn_0e_6_usa
'''
import MySQLdb
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).filter_by(id=2)\
                                     .order_by(State.id).all():
        state.name = "New Mexico"
    session.commit()
    session.close()
