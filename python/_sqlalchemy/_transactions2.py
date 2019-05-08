# https://docs.sqlalchemy.org/en/13/core/connections.html#using-transactions
"""
The Connection object provides a begin() method which returns a Transaction object.
This object is usually used within a try/except clause so that it is guaranteed to
invoke Transaction.rollback() or Transaction.commit():
"""
connection = engine.connect()
trans = connection.begin()
try:
    r1 = connection.execute(table1.select())
    connection.execute(table1.insert(), col1=7, col2='this is some data')
    trans.commit()
except:
    trans.rollback()
    raise


"""
The above block can be created more succinctly using context managers, either given an Engine:
"""
# runs a transaction
with engine.begin() as connection:
    r1 = connection.execute(table1.select())
    connection.execute(table1.insert(), col1=7, col2='this is some data')


"""
Or from the Connection, in which case the Transaction object is available as well:
"""
with connection.begin() as trans:
    r1 = connection.execute(table1.select())
    connection.execute(table1.insert(), col1=7, col2='this is some data')
