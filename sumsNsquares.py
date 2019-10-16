# sum of square
# minus
# square of sum

# by jumBop

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
    
if __name__=='__main__':
    test = 100

    print(diff(squareSum(test),sumSquare(test)))
