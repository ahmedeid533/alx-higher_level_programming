#!/usr/bin/python3
from sqlalchemy import create_engine
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

for state in engine["State"].order_by(engine["State"].id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
