"""
Inserting Records

There are several ways to insert records into the database. The most basic way is to use
the insert() method of the Table instance and pass values of the columns as keyword args
to the values() method.
"""

ins = customers.insert().values(
    first_name='Bryan',
    last_name='Andrade',
    username='bryand1',
    email='bryand1@gmail.com',
    address='1535 6th St',
    town='Santa Monica'
)

# To view the SQL this code would generate type the following:
# str(ins)

# When the query is run against the database the dialect will replace the bind parameters
# with the actual values. The dialect will also escape the values to mitigate the risk of
# SQL injection.

# We can view the values that will replace the bind parameters by compiling the insert stmt.
# ins.compile().params

conn = engine.connect()
r = conn.execute(ins)

# The execute() method returns an object of type ResultProxy. The ResultProxy provides several
# attributes, one of them is called inserted_primary_key which returns the primary key of the
# records just inserted.

# Another way to create insert statement is to use the standalone insert() function from sqlalchemy.
from sqlalchemy import insert

ins = insert(customers).values(
    first_name='Bryan'
    # ...
)

r = conn.execute(ins)
r.inserted_primary_key

"""
Multiple Inserts

Instead of passing values to the values() method as keyword args, we can also pass them to the
execute() method.
"""

ins = insert(customers)

r = conn.execute(ins,
    first_name='Bryan',
    last_name='Andrade'
    # ...
)
r.inserted_primary_key  # returns a List

r = conn.execute(ins, [
    {
        "first_name": "Bryan"
    },
    {
        "first_name": "John"
    }
])

r.rowcount  # 2

