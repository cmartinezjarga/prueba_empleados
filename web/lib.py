import os


def get_pardir():

    return os.path.realpath(os.path.join(__file__, os.pardir))