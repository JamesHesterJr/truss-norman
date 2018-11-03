
import unittest
import dateutil.parser
import pytz
from pytz import timezone

import norman

class TestTimestampTimezoneConversionRule(unittest.TestCase):

    def test_it_converts_timestamp_from_eastern_to_pacific(self):
    	
    	rule = norman.TimestampTimezoneConversionRule()
    	timestamp = "4/1/11 11:00:00 PM"
    	
    	actual = rule.normalize(timestamp)
    	expected = timezone('US/Pacific').localize(dateutil.parser.parse(timestamp)).astimezone(timezone('US/Eastern'))

    	self.assertEqual(expected, actual)