from collections import namedtuple
from datetime import datetime
import json
from typing import Any, Iterable

Transaction = namedtuple('Transaction', ['id', 'customer', 'datetime', 'amount', 'location'])


def create(record: Iterable) -> Transaction:
    return Transaction._make(record)


def annotate_location(tx: Transaction, zipcode: str) -> Transaction:
    return tx._replace(location=zipcode)


def to_json(tx: Transaction) -> str:
    return json.dumps(tx._asdict(), default=serializer)


def serializer(a: Any) -> Any:
    if isinstance(a, datetime):
        return a.strftime("%Y-%m-%d %H:%M:%S")
    return a


def main():
    record1 = [1, 100, datetime(2019, 7, 14), 75.90, None]
    tx1 = create(record1)
    print(tx1)
    tx1_loc = annotate_location(tx1, "07666")
    print(tx1_loc)
    print(to_json(tx1_loc))


if __name__ == '__main__':
    main()
