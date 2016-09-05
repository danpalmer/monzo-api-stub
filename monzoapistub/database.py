"""
No, this is not a real DB, but it is a big blob of global mutable state...
...like a DB.
"""
import collections

from . import datatypes


db = {
    'user': None,
    'accounts': collections.OrderedDict(),
    'transactions': [],
}


def init(num_accounts):
    db['user'] = datatypes.User()

    for _ in range(num_accounts):
        account = datatypes.Account(db['user'])
        db['accounts'][account.accout_id] = account
