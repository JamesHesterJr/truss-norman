
import unittest
import norman

class TestUppercaseRule(unittest.TestCase):

    def test_it_makes_name_upper(self):
        rule = norman.UppercaseRule()

        name = "Superman übertan"
        actual = rule.normalize(name)

        self.assertTrue(actual.isupper())