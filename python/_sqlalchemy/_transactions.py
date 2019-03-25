"""
Transactions

A transaction is a way to execute a set of SQL statements such that either all
of the statements are executed successfully or nothing at all. If any of the
statement involved in the transaction fails then the database is returned to
the state it was in before the transaction was initiated.

We currently have two orders in the database. To fulfill an order we need to perform
the following two actions:
    1. Subtract the quantity of ordered items from the items table
    2. Update the date_shipped column to contain the datetime value.

Both of these actions must be performed as a unit to ensure data integrity.

The Connection object provides a begin() method, which starts the transaction and
returns an object of type Transaction. The Transaction object in turn provides
rollback() and commit() method, to rollback and commit the transaction, respectively.

In the following listing we define dispatch_order() method which accepts order_id
as an argument, and performs the above mentioned actions using transaction.
"""

from sqlalchemy.exc import IntegrityError


def dispatch_order(order_id):

    # check whether order_id is valid or not
    r = conn.execute(select([func.count('*')]).where(orders.c.id == order_id))
    if not r.scalar():
        raise ValueError('Invalid order id: {}'.format(order_id))

    # fetch items in the order
    s = select([order_lines.c.item_id, order_lines.c.quantity]).where(
        order_lines.c.order_id == order_id
    )

    rs = conn.execute(s)
    ordered_items_list = rs.fetchall()

    # start transaction
    t = conn.begin()

    try:
        for i in ordered_items_list:
            u = update(items).where(
                items.c.id == i.item_id
            ).values(quantity = items.c.quantity - i.quantity)

            rs = conn.execute(u)
        u = update(orders).where(orders.c.id == order_id).values(date_shipped=datetime.now())
        rs = conn.execute(u)
        t.commit()
        print('Transaction completed')
    except IntegrityError as e:
        print(e)
        t.rollback()
        print('Transaction failed')

