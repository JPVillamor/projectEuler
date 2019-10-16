# smallest multiple
# of all numbers 1-20

# by jumBop

def factorial(n):
    fac = n

    for i in range(1,n):
        fac *= i

    return fac

def isPrime(n):
    for i in range(n//2,1,-1):
        if n%i==0:
            return 0
    return 1

if __name__=='__main__':
    test = 20
    Factors = []
    found = 0

    for i in range(1,test//2+1):
        if not isPrime(i):
            Factors.append(i)
    for i in range(test, test//2, -1):
        Factors.append(i)

    print(Factors)

    n = test

    while found == 0:
        failed = 0
        for i in Factors:
            if n%i != 0:
                n += test
                failed = 1
                break
        if not failed:
            print(n)
            break
