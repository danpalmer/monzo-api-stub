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


def init():
    db['user'] = datatypes.User()
