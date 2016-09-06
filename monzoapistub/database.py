"""
No, this is not a real DB, but it is a big blob of global mutable state...
...like a DB.
"""
import collections

from . import datatypes


db = {
    'user': None,
    'accounts': collections.OrderedDict(),
    'transactions': {},
    'merchant_groups': {},
    'merchants': {},
}


def init(num_accounts, currency):
    db['user'] = datatypes.User()

    merchant_groups = [datatypes.MerchantGroup() for _ in range(100)]
    db['merchant_groups'] = dict(
        (m.merchant_group_id, m) for m in merchant_groups
    )

    merchants = [datatypes.Merchant(merchant_groups) for _ in range(200)]
    db['merchants'] = dict((m.merchant_id, m) for m in merchants)

    for _ in range(num_accounts):
        account = datatypes.Account(db['user'], currency)
        db['accounts'][account.account_id] = account

        transactions = sorted([
            datatypes.Transaction(account, merchants) for _ in range(1000)
        ], key=lambda x: x.created)

        db['transactions'][account.account_id] = collections.OrderedDict([
            (t.transaction_id, t) for t in transactions
        ])
