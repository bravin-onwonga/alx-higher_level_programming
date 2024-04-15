#!/usr/bin/python3
"""
Module to list state.name ordered by id
"""

import MySQLdb, sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class representing our table states
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    username, passwd, dbName = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, passwd, dbName), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
