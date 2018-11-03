
import unittest
import norman

class TestFloatingPointSecondsRule(unittest.TestCase):

    def test_it_converts_time_into_floating_point_seconds(self):
        rule = norman.FloatingPointSecondsRule()

		# HH:MM:SS.MS
        time = "1:23:32.123"

		# HH * 60 * 60 + MM * 60 + SS.MS
        expected = 5012.123
     
        actual = rule.normalize(time)
        
        self.assertEqual(actual, expected)