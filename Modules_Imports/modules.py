#Built in modules and functions
import math

# importing only required part from the module
from math import ceil
from math import floor

# Importing our own module
import calculator

# From own module importing only required functionalities
from calculator import multiply
from calculator import divide


print(math.pi)
print(math.sqrt(16))
print(math.isqrt(16))
print(math.pow(3,3))




print("Using the imported required modules functionalities....")
print(ceil(10.3))
print(floor(10.8))




a = 10
b : int = 20

print(calculator.add(a, b))
print(calculator.subtract(b, a))

print(multiply(a, b))
print(divide(b, a))


