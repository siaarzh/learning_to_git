class Adder(object):
	'''
	Basic Adder class
	'''

	def __init__(self):
		pass

	def add(self, *args):

		for i in args:
			product = 1
			product = product+i
		return product