import random

from faker import Faker


fake = Faker()

class User(object):
    def __init__(self):
        self.name = fake.name()
        self.user_id = generate_monzo_id('cus')


class Account(object):
    def __init__(self, user, currency):
        self.account_id = generate_monzo_id('acc')
        self.description = '%s\'s %s' % (user.name, fake.word().title())
        self.created = fake.date_time_between(start_date='-1y', end_date='now')
        self.balance = random.randint(100, 100000)
        self.spend_today = random.randint(100, 10000)

        if currency == 'random':
            self.currency = fake.currency_code()
        else:
            self.currency = currency


def generate_token():
    return fake.sha1(raw_output=False)


def generate_monzo_id(kind):
    return '%s_%d%s' % (
        kind,
        fake.pyint(),
        fake.pystr(min_chars=20, max_chars=20),
    )
