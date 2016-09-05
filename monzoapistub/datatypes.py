from faker import Faker


fake = Faker()


def generate_token():
    return fake.sha1(raw_output=False)
