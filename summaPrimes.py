# summation of primes

# by jumBop

from libEuler import *

if __name__=='__main__':
    limit = 2000000
    total = 0

    for i in range(2, limit):
        if isPrime(i):
            total += i

    print(total)
