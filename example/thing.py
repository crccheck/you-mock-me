import requests


class Foo():
    def __init__(self):
        pass

    def thing(self):
        raise NotImplementedError()


def get_that_thing():
    response = requests.get('https://example.com')
    assert response.ok
    return response.text


def get_that_json():
    response = requests.get('https://example.com/index.json')
    assert response.ok
    return response.json()['name']


def process_that_thing():
    # get data from sql
    # do a sum on a column
    # return that sum
    pass
