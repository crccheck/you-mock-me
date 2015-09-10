"""
mock an external web request
"""
from unittest import TestCase
try:
    from unittest import mock
except:
    # Python 2
    import mock

from example.thing import get_that_thing, get_that_json


class ExcerciseTests(TestCase):
    @mock.patch('example.thing.requests')
    def test_1_thing(self, mock_requests):
        #################################
        mock_response = mock.Mock()
        mock_response.ok = True
        mock_response.text = 'xyzzy'
        mock_requests.get.return_value = mock_response
        #################################

        self.assertEqual(get_that_thing(), 'xyzzy')
        self.assertTrue(mock_requests.get.called)

    @mock.patch('example.thing.requests')
    def test_json_response(self, mock_requests):
        #################################
        mock_response = mock.Mock()
        mock_response.ok = True
        mock_response.json.return_value = {'name': 'xyzzy'}
        mock_requests.get.return_value = mock_response
        #################################

        self.assertEqual(get_that_json(), 'xyzzy')
