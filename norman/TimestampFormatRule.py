
# The Timestamp column should be formatted in ISO-8601 format.

import datetime
import dateutil.parser

class TimestampFormatRule(object):

	def normalize(self, timestamp):
		return dateutil.parser.parse(timestamp).isoformat()

