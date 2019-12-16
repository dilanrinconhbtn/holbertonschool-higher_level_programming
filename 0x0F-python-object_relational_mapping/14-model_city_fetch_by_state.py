#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    N_session = Session()

    for class_instance in N_session.query(State, City).filter(State.id ==
                                                                City.state_id):
        print("{}: ({}) {}".format(class_instance.State.name,
                                   class_instance.City.id,
                                   class_instance.City.name))
    N_session.close()