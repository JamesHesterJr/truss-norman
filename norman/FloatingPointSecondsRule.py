
# The columns `FooDuration` and `BarDuration` are in 1
# format (where MS is milliseconds); please convert them to a floating
# point seconds format.

class FloatingPointSecondsRule(object):

	def normalize(self, time):

		units = time.split(":")
		seconds = int(units[0]) * 60 * 60 + int(units[1]) * 60 + float(units[2])
		
		return seconds
