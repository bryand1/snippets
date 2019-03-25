"""
Deleting Records

To delete records we use the delete() function.
"""
from sqlalchemy import delete

s = delete(customers).where(
    customers.c.username.like('pablo%')
)

