#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, passwd, dbName = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, passwd, dbName), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all([State(name="California")])

    session.commit()

    state = session.query(State).filter(State.name == "California").first()

    session.add_all([City(name="San Francisco", state_id=state.id)])

    session.commit()

    session.close()
