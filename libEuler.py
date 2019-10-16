# library for Project Euler Submissions

# by jumBop

def isPrime(n):
    for i in range(n//2,1,-1):
        if n%i==0:
            return 0
    return 1

def squareSum(n):
    total = 0
    for i in range(1,n+1):
        total += i**2

    return total

def sumSquare(n):
    total = 0
    for i in range(1,n+1):
        total += i

    return total**2

def diff(m,n):
    d = m-n

    if d > 0:
        return d
    return -d

def isPalin(n):
    nstr = str(n)
    for x in range(len(nstr)//2+1):
        if nstr[x] == nstr[-x-1]:
            continue
        else:
            return 0
    return 1

def factorial(n):
    fac = n

    for i in range(1,n):
        fac *= i

    return fac
