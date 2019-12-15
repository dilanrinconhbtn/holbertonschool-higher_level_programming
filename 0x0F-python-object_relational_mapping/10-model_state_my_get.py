#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    name_search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    N_session = Session()

    state_found = N_session.query(State).filter(State.name == (sys.argv[4]))

    try:
        print(state_found[0].id)
    except:
        print("Not found")

    N_session.close()
