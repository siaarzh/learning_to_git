from utils import adder, multiplier

A = adder.Adder()
P = multiplier.Multiplier()

numbers = [1, 2, 3]

print("Sum = {}".format(A.add(*numbers)))
print("Product = {}".format(P.mult(*numbers)))