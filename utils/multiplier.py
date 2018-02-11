class Multiplier(object):

    def __init__(self):
        pass

    def mult(self, *args):
        product = 1
        for i in args:
            product = product*i
        return product