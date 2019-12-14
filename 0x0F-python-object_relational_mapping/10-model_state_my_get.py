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
    state_found = 0
    for instance in N_session.query(State).order_by(State.id):
        if instance.name == name_search:
            print("{}".format(instance.id))
            state_found += 1

    if state_found == 0:
        print("Not found")
    N_session.close()
