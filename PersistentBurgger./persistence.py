import operator
from functools import reduce
def persistence(n):
    i = 0
    while n >= 10:
        n=reduce(operator.mul,[int(x) for x in str(n)], 1)
        i+=1
    return i