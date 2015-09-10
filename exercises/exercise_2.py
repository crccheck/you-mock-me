"""
mock.patch
"""
from unittest import TestCase
try:
    from unittest import mock
except:
    # Python 2
    import mock

from example.thing import Foo


class ExcerciseTests(TestCase):
    @mock.patch('example.thing.Foo.thing')
    def test_1_thing(self, mock_thing):
        obj = Foo()

        #################################
        mock_thing.return_value = 'xyzzy'
        #################################

        self.assertEqual(obj.thing(), 'xyzzy')
