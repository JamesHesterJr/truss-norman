
import unittest
import norman

class TestStripper(unittest.TestCase):

    def test_it_splits_without_any_quotes(self):
        splitter = norman.Splitter()

        string = "example,wonderful,should work"

        actual = splitter.split(string)
        expected = ["example", "wonderful", "should work"]

        self.assertEqual(actual, expected)

    def test_it_splits_with_single_quotes(self):
        splitter = norman.Splitter()

        string = "example,'staying, together, now!',should work"

        actual = splitter.split(string)
        expected = ["example","'staying, together, now!'","should work"]

        self.assertEqual(actual, expected)


    def test_it_splits_with_double_quotes(self):
        splitter = norman.Splitter()

        string = 'example,"staying, together, now!",should work'

        actual = splitter.split(string)
        expected = ["example",'"staying, together, now!"',"should work"]

        self.assertEqual(actual, expected)