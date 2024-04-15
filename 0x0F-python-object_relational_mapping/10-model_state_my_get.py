#!/usr/bin/python3
"""
Module to list state.name ordered by id
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()


if __name__ == "__main__":
    if (len(sys.argv) == 5):
        username, passwd, dbName = sys.argv[1:4]
        state_name = str(sys.argv[4])

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                            (username, passwd, dbName), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            state = session.query(State).filter(State.name ==  state_name).order_by(State.id).one()
            if (state):
                print("{}".format(state.id))
            else:
                print("Nothing")
        except NoResultFound:
            print("Nothing")
        except AttributeError:
            print("Nothing")
        finally:
            session.close()
