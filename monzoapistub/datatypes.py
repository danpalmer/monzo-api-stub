from faker import Faker


fake = Faker()

class User(object):
    def __init__(self):
        self.name = fake.name()
        self.user_id = generate_monzo_id('cus')


def generate_token():
    return fake.sha1(raw_output=False)


def generate_monzo_id(kind):
    return '%s_%d%s' % (
        kind,
        fake.pyint(),
        fake.pystr(min_chars=20, max_chars=20),
    )
