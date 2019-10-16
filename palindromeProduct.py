# palindrome product
# finds the largest palindrome product of two numbers.

# by jumBop

def isPalin(n):
    nstr = str(n)
    for x in range(len(nstr)//2+1):
        if nstr[x] == nstr[-x-1]:
            continue
        else:
            return 0
    return 1

if __name__=='__main__':
    answer = 0

    for x in range(999,99,-1):
        for y in range(999,99,-1):
            if (isPalin(x*y)) and (x*y>answer):
                answer = x*y

    print(answer)
