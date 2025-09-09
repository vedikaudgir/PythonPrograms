import sys

array = [0, 1, 10**10, 100**100]

for i in array:
    print(f"Size of {i} is {sys.getsizeof(i)} bytes")