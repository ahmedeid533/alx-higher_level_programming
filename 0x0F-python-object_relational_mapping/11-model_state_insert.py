#!/usr/bin/python3
"""import modules"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_State = State(name='Louisiana')
    session.add(new_State)
    new_opj = session.query(State).filter_by(name='Louisiana').first()
    print(new_opj.id)
    session.commit()
