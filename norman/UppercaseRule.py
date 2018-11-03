
# All name columns should be converted to uppercase. There will be
# non-English names.

class UppercaseRule(object):
	
	def normalize(self, name):
		return name.upper()

	