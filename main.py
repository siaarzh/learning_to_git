from utils import adder, multiplier

A = adder.Adder()
P = multiplier.Multiplier()

numbers = [1, 2, 3, 4]

print("Sum = {}".format(A.add(*numbers)))
# line for checking SSH connection
print("Product = {}".format(P.mult(*numbers)))
