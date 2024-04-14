#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define Base class
Base = declarative_base()

# Define State class that corresponds to the State table
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username, passwd, dbName = sys.argv[1:]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, passwd, dbName), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print States ordered by ID
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
