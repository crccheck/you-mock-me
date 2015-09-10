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
