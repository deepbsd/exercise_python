#!/usr/bin/env python3

from functools import reduce
import operator
    


def largest_product(ser, num):
    lst = list(ser)
    lst = list(map(int, lst))
    if num > len(lst) or num < 0:
        raise ValueError('Wrong size')

    def prod(iterable):
        return reduce(operator.mul, iterable, 1)
    
    products = []
    for n in range(len(lst)-num+1):
        products.append( prod(lst[n:n+num]) )  
    return max(products)


if __name__ == "__main__":
    print(largest_product("0123456789", 3))