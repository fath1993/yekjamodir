import random


def generate_otp():
    code = str(random.randrange(528899, 998899))
    return code


def generate_api_token():
    code = str(random.randrange(528890, 998890)) + str(random.randrange(528890, 998890)) + \
           str(random.randrange(528890, 998890))
    return code