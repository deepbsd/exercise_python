#!/usr/bin/env python3

def sieve(num):
    primes = []
    for n in range(2,num+1):
        for x in range(2,n):
            if n%x==0:
                #print(n, 'equals to', x, '*', n//x)
                break
        else:
            primes.append(n)

    return primes

if __name__ == "__main__":
    
    print(sieve(120))