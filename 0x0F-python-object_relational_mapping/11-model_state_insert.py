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
    opj = Session()
    state = State(name='Louisiana')
    opj.add(state)
    new_opj = opj.query(State).filter_by(name='Louisiana').first()
    print(new_opj.id)
    opj.commit()
