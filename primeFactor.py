# prime factor finder

# by jumBop

# test = 600851475143

def isPrime(n):
    for i in range(n//2,1,-1):
        if n%i==0:
            return 0
    return 1

def findFactor(n):
    for i in range(2,n):
        if isPrime(i):
            if n%i==0:
                n/=i
                if isPrime(n):
                    print(n)
                    break

if __name__=='__main__':
    findFactor(600851475143)
