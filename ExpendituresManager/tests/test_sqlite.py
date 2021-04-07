import os
from datetime import datetime
from random import random

from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ExpendituresManager.models.row import create_models
from ExpendituresManager.utilities import generate_sqlite_uri, THIS_DIR, string_to_date

rn_0 = str(int(random() * 100000) // 100)
rn_1 = str(int(random() * 100000) // 100)
user = rn_0 + "_PYTEST_" + rn_1


def test_db_creation():
    engine = create_engine(generate_sqlite_uri(THIS_DIR + "\\tests\\" + user + ".db"), echo=True)
    base = declarative_base()
    base.metadata.create_all(engine)
    assert_1 = user + ".db" in os.listdir(THIS_DIR + "\\tests\\")

    os.remove(THIS_DIR + "\\tests\\" + user + ".db")

    assert assert_1


def test_db_population():
    engine = create_engine(generate_sqlite_uri(THIS_DIR + "\\tests\\" + user + ".db"), echo=True)
    Base = declarative_base()

    Stock = create_models(Base, 'testTable')
    Base.metadata.create_all(engine)

    new_row_attributes = (datetime.today().date(), 'testShop', 'testDescription', 10., 'testEvent', 'Test')

    tick = Stock(date=new_row_attributes[0], shop=new_row_attributes[1], description=new_row_attributes[2], cost=new_row_attributes[3], event=new_row_attributes[4], expenditure_type=new_row_attributes[5])
    Session = sessionmaker(bind=engine)

    session = Session()

    session.add(tick)
    session.commit()

    query_all = session.query(Stock).all()
    assert_0 = len(query_all) == 1
    session.close()
    #
    # query = query_all[0]
    #
    # assert_1 = []
    # i = 0
    # for attribute in ("date", "shop", "description", "cost", "event", "expenditure_type"):
    #     assert_1.extend([query.__getattribute__(attribute) == new_row_attributes[i]])
    #     i += 1
    # assert_1 = assert_1 == [True, True, True, True, True, True]

    os.remove(THIS_DIR + "\\tests\\" + user + ".db")
    assert assert_0
    # if assert_0 and assert_1:
    #     assert True
    # else:
    #     assert False

def test_db_writing_and_reading():
    engine = create_engine(generate_sqlite_uri(THIS_DIR + "\\tests\\" + user + ".db"), echo=True)
    Base = declarative_base()

    Stock = create_models(Base, 'testTable')
    Base.metadata.create_all(engine)

    new_row_attributes = (datetime.today().date(), 'testShop', 'testDescription', 10., 'testEvent', 'Test')

    tick = Stock(date=new_row_attributes[0], shop=new_row_attributes[1], description=new_row_attributes[2], cost=new_row_attributes[3], event=new_row_attributes[4], expenditure_type=new_row_attributes[5])
    Session = sessionmaker(bind=engine)

    session = Session()

    session.add(tick)
    session.commit()

    query_all = session.query(Stock).all()

    query = query_all[0]

    assert_1 = []
    i = 0
    for attribute in ("date", "shop", "description", "cost", "event", "expenditure_type"):
        assert_1.extend([query.__getattribute__(attribute) == new_row_attributes[i]])
        i += 1
    assert_1 = assert_1 == [True, True, True, True, True, True]
    session.close()
    os.remove(THIS_DIR + "\\tests\\" + user + ".db")
    assert assert_1
