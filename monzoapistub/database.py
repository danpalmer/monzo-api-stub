"""
No, this is not a real DB, but it is a big blob of global mutable state...
...like a DB.
"""

from . import datatypes


db = {
    'user': None,
    'accounts': [],
    'transactions': [],
}


def init(num_accounts):
    db['user'] = datatypes.User()

    for _ in range(num_accounts):
        db['accounts'].append(datatypes.Account(db['user']))
