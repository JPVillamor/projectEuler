# special pythagorean triplet
# a+b+c == 1000

# by jumBop

import math

if __name__=='__main__':
    for h in range(1000,1,-1):
        for short in range(1,1000):
            long = 1000 - h - short
            if long <= short:
                break
            if h**2 == (long**2)+(short**2):
                print(short)
                print(long)
                print(h)
                print(short*long*h)
