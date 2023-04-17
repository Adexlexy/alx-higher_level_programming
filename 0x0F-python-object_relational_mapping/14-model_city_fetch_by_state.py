#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa
    """

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    # Set up the tables in the database
    Base.metadata.create_all(engine)
    # Configuring session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query all the instances in the City and State tables
    instances = session.query(City, State).filter(
        City.state_id == State.id).all()
    # print all the instances in the City and State tables
    for inst in instances:
        print("{}: ({}) {}".format(inst[1].name, inst[0].id, inst[0].name))
    # commit the changes
    session.commit()
    # close the session
    session.close()