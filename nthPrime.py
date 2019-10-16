# find the nth prime number

# by jumBop

def isPrime(n):
    for i in range(n//2,1,-1):
        if n%i==0:
            return 0
    return 1

if __name__=='__main__':
    x = 0
    y = 2

    limit = 6
    
    while x <= limit:
        if isPrime(y):
            x += 1
            if x == limit:
                break
        y += 1

    print(y)
