
import unittest
import dateutil.parser

import norman

class TestTimestampFormatRule(unittest.TestCase):

    def test_it_formats_timestamp_to_valid_format(self):

        rule = norman.TimestampFormatRule()

        timestamp = "4/1/11 11:00:00 PM"

        actual = rule.normalize(timestamp)
        expected = dateutil.parser.parse(timestamp).isoformat()

        self.assertEqual(expected, actual)