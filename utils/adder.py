class Adder(object):
    '''
	Basic Adder class
	'''

    def __init__(self):
        pass

    def add(self, *args):
        sum = 0
        for i in args:
            sum = sum + i
        return sum
