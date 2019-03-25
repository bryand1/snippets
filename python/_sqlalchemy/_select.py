"""
Selecting Records

To select records we use select() method of the Table object
"""

s = customers.select()

# str(s)
# 'SELECT customers.id, customers.first_name, customers.last_name, customers.username,...

# Another way to create SELECT query is to use the standalone select() function. It accepts
# a list of tables or columns from where to retrieve data.

from sqlalchemy import select

s = select([customers])

# To send the query to the database we use the execute():

r = conn.execute(s)
r.fetchall()

# The fetchall() method loads all the results into memory at once. Thus, it is not very efficient
# on a large reset set. Alternatively, you can use for loop to iterate over the result set.
rs = conn.execute(s)
for row in rs:
    print(row)

"""
Here is a list of some common methods and attributes of the ResultProxy object

fetchone()
fetchmany(size=None)
fetchall()
first()
rowcount
keys()
scalar()
"""

r = conn.execute(s)
row = r.fetchone()
row['id'], row['first_name']  # access column data via column name
row[0], row[1]  # access column data via column index position
row[customers.c.id], row[customers.c.first_name]  # access column data via Column object
row.id, row.first_name  # access column data via attribute

# To access data from multiple tables simply pass comma separated list of Table instances
# to the select() function.
select([tableOne, tableTwo])

"""
Filtering Records

To filter records we use where() method. It accepts a condition and adds a WHERE clause to
the SELECT statement.
"""

s = select([items]).where(
    items.c.cost_price > 20
)

str(s)
r = conn.execute(s)
r.fetchall()

# AND
s = select([items]).\
where(
    (items.c.cost_price + items.c.selling_price > 50) &
    (items.c.quantity > 10)
)

# OR
s = select([items]).\
where(
    (items.c.cost_price > 200 ) |
    (items.c.quantity < 5)
)

# Conjunctions: and_(), or_(), not_()
s = select([items]).\
where(
    and_(
        items.c.quantity >= 50,
        items.c.cost_price < 100,
    )
)

# Other Common Comparison Operators

# IS NULL
s = select([orders]).where(
    orders.c.date_shipped == None
)

# IS NOT NULL
s = select([orders]).where(
    orders.c.date_shipped != None
)

# IN 
s = select([customers]).where(
    customers.c.first_name.in_(["Sarah", "John"])
)

# NOT IN
s = select([customers]).where(
    customers.c.first_name.notin_(["Sarah", "John"])
)

# BETWEEN

s = select([items]).where(
    items.c.cost_price.between(10, 20)
)

# NOT BETWEEN

s = select([items]).where(
    not_(items.c.cost_price.between(10, 20))
)

# LIKE

s = select([items]).where(
    items.c.name.like("Wa%")
)

# ILIKE
s = select([items]).where(
    items.c.name.ilike("wa%")
)

# NOT LIKE
s = select([items]).where(
    not_(items.c.name.like("wa%"))
)

# ORDERING RESULT
from sqlalchemy import desc
s = select([items]).where(
    items.c.quantity > 10
).order_by(desc(items.c.cost_price))


# DISTINCT
s = select([customers.c.town]).where(customers.c.id  < 10).distinct()

"""
Limiting Results

The limit() method adds the LIMIT clause to the SELECT statement. It accepts an integer,
which indicates the number of rows to return. For example:

"""

s = select([items]).order_by(
    items.c.quantity
).limit(2)

s = select([items]).order_by(
    items.c.quantity
).limit(2).offset(2)

"""
Limiting Columns

The SELECT statements we have created have returned data from all the columns of the table.
We can limit the number of fields returned by the query by passing the name of the fields
as a list to the select() function.
"""
s = select([items.c.name, items.c.quantity]).where(
    items.c.quantity == 50
)

# Just as in SQL, we can perform simple calculations on rows retrieved
s = select([
        items.c.name,
        items.c.quantity,
        items.c.selling_price * 5
    ]).where(
    items.c.quantity ==  50
)


# We can assign a label to a column or expression using the label() method,
# which works by adding an AS subclause to the SELECT statement.
s = select([
        items.c.name, 
        items.c.quantity, 
        (items.c.selling_price * 5).label('price') 
    ]).where(
    items.c.quantity ==  50
)

"""
Accessing Built-in Functions

To access built-in functions provided by the database we use func object.
The following listing shows how to use date/time, mathematical and string
functions found in PostgreSQL database.
"""

from sqlalchemy.sql import func

c = [

    ##  date/time functions  ##

    func.timeofday(),
    func.localtime(),
    func.current_timestamp(),
    func.date_part("month", func.now()),
    func.now(),

    ##  mathematical functions  ##

    func.pow(4,2),
    func.sqrt(441),
    func.pi(),
    func.floor(func.pi()),
    func.ceil(func.pi()),

    ##  string functions  ##

    func.lower("ABC"),
    func.upper("abc"),
    func.length("abc"),
    func.trim("  ab c  "),
    func.chr(65),
]

s = select(c)
rs = conn.execute(s)
rs.keys()
rs.fetchall()

# You also have access to the aggregate functions via the func object

from sqlalchemy.sql import func

c = [
    func.sum(items.c.quantity),
    func.avg(items.c.quantity),
    func.max(items.c.quantity),
    func.min(items.c.quantity),
    func.count(customers.c.id),
]

s = select(c)

"""
Grouping Results

Grouping results is done via GROUP BY clause. It is commonly used in conjunction with
the aggregate functions. We add GROUP BY clause to the select statement using group_by()
It accepts one or more columns and groups the rows according to the values in the column.
"""
c = [
    func.count('*').label('count'),
    customers.c.town
]

s = select(c).group_by(customers.c.town)

# HAVING
from sqlalchemy.sql import func
 
c = [
    func.count("*").label('count'),
    customers.c.town      
]
 
s = select(c).group_by(customers.c.town).having(func.count("*") > 2)

"""
Joins

The Table instance provides the following two methods to create joins:

    1. join() - creates inner join
    2. outerjoin() - creates outer join (LEFT OUTER JOIN to be specific)

The inner join returns only the rows which match the join condition,
whereas the outer join returns the rows which match the join condition
as well as some additional rows.

Both methods accept a Table instance, figures out the join condition based
on the foreign key relationship and returns a JOIN construct.
"""
customers.join(orders)
customers.join(items, customers.c.address.like(customers.c.first_name + '%'))

"""
When we specify tables or list of columns in the select() function, SQLAlchemy
automatically places those tables in the FROM clause. However, when we use join,
we know exactly the tables we want in the FROM clause, so we use the select_from()
method. However, if we want we can use select_from() in queries not involving joins too.
"""
s = select([
    customers.c.id,
    customers.c.first_name
]).select_from(
    customers
)

s = select([
            orders.c.id,
            orders.c.date_placed
]).select_from(
    orders.join(customers)
).where(
    and_(
        customers.c.first_name == "John",
        customers.c.last_name == "Green",
    )
)

s = select([
    orders.c.id.label('order_id'),
    orders.c.date_placed,
    order_lines.c.quantity,
    items.c.name,

]).select_from(
    orders.join(customers).join(order_lines).join(items)
).where(
    and_(
        customers.c.first_name == "John",
        customers.c.last_name == "Green",
    )
)

# LEFT JOIN
s = select([        
    customers.c.first_name,
    orders.c.id,
]).select_from(
    customers.outerjoin(orders)
)

# FULL OUTER JOIN
s = select([
    customers.c.first_name,
    orders.c.id,
]).select_from(
    orders.outerjoin(customers, full=True)
)

"""
Casting

Casting (converting) data from one type to another is a common operation and is
done via cast() function from the sqlalchemy package.
"""
from sqlalchemy import cast, Date

s = select([
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10, 2)),
    cast('2010-12-01', DateTime),
    cast('2010-12-01', Date),
])

"""
Unions

The SQL UNION operator allows us to combine result set of multiple SELECT statements.
To add UNION operator to our SELECT statement we use union() function.
"""
u = union(
    select([items.c.id, items.c.name]).where(items.c.name.like('Wa%')),
    select([items.c.id, items.c.name]).where(items.c.name.like('%e%')),
).order_by(desc('id'))

# By default, union() removes all the duplicate rows from the result set. If you
# want to keep the duplicates use union_all()
s = union_all(
    select([items.c.id, items.c.name]).where(items.c.name.like("Wa%")),
    select([items.c.id, items.c.name]).where(items.c.name.like("%e%")),
).order_by(desc("id"))

"""Creating Subqueries

We can also access data from multiple tables using subqueries.

The following query returns the id and name of the items ordered by John Green:
"""

s = select([items.c.id, items.c.name]).where(
    items.c.id.in_(
        select([order_lines.c.item_id]).select_from(customers.join(orders).join(order_lines)).where(
                and_(
                    customers.c.first_name == 'John',
                    customers.c.last_name == 'Green',
                    orders.c.id == 1
                )
        )
    )
)

# This query can also be written using joins
s = select([items.c.id, items.c.name]).select_from(customers.join(orders).join(order_lines).join(items)).where(
    and_(
        customers.c.first_name == 'John',
        customers.c.last_name == 'Green',
        orders.c.id == 1
    )
)

"""
Raw Queries

SQLAlchemy also gives you the flexibility to execute raw SQL using the text() function.
For example, the following SELECT statement returns all the orders, along with the items
ordered by John Green.

"""
from sqlalchemy.sql import text
 
s = text(
"""
SELECT
    orders.id as "Order ID", orders.date_placed, items.id, items.name
FROM
    customers
INNER JOIN orders ON customers.id = orders.customer_id
INNER JOIN order_lines ON order_lines.order_id = orders.id
INNER JOIN items ON items.id= order_lines.item_id
where customers.first_name = :first_name and customers.last_name = :last_name
"""
)
rs = conn.execute(s, first_name="John", last_name='Green')

# The text() function can also be embedded inside a select() construct.
s = select([items]).where(
    text("items.name like 'Wa%'")
).order_by(text("items.id desc"))

