"""
Updating Records

Updating records is achieved using the update() function. For example, the following
query updates the selling_price and quantity of Water Bottle to 30 and 60, respectively.
"""

from sqlalchemy import update

s = update(items).where(
    items.c.name == 'Water Bottle'
).values(
    selling_price=30,
    quantity=60
)

