
# The Timestamp column should be assumed to be in US/Pacific time;
# please convert it to US/Eastern.

import dateutil.parser
import pytz
from pytz import timezone

class TimestampTimezoneConversionRule(object):

	def normalize(self, timestamp):
		return timezone('US/Pacific').localize(dateutil.parser.parse(timestamp)).astimezone(timezone('US/Eastern'))