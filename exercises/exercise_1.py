"""
mock.patch
"""
from unittest import TestCase
try:
    from unittest import mock
except:
    # Python 2
    import mock


class ExcerciseTests(TestCase):
    def test_mock_attribute_can_be_arbitrary(self):
        foo = mock.MagicMock()

        # BEGIN
        # END

        self.assertEqual(foo.bar, 'xyzzy')

    def test_mock_return_value_can_be_set(self):
        foo = mock.MagicMock()

        # BEGIN
        # END

        self.assertEqual(foo.bar(), 'xyzzy')

    def test_mock_side_effect_as_multiple_returns(self):
        foo = mock.MagicMock()

        # BEGIN
        # END

        self.assertEqual(foo.bar(), 'remember')
        self.assertEqual(foo.bar(), 'the')
        self.assertEqual(foo.bar(), 'alamo')

    def test_mock_side_effect_can_raise_exceptions(self):
        foo = mock.MagicMock()

        # BEGIN
        # END

        with self.assertRaises(AttributeError):
            foo.bar()

    def test_mock_side_effect_combination(self):
        foo = mock.MagicMock()

        # BEGIN
        # END

        self.assertEqual(foo.bar(), 'remember')
        self.assertEqual(foo.bar(), 'the')
        with self.assertRaises(KeyError):
            foo.bar()

    def test_mock_with_chained_calls(self):
        foo = mock.MagicMock()
        # BEGIN
        # END
        self.assertEqual(foo.bar().baz(), 'xyzzy')
