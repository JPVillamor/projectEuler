# largest product of
# adjacent numbers in series

# by jumBop

def getContents(filename):
    f = open(filename, 'r')
    if f.mode == 'r':
        contents = f.read()
        return contents
    else:
        return 0

def shiftList(li):
    del li[0]

def findProduct(li):
    answer = 1
    
    for i in li:
        answer *= in

    return answer

if __name__=='__main__':
    series = getContents('series.txt')
    adjacent = []
    largeList = []
    largest = 0
    size = 13

    for i in series:
        if i == '\n':
            continue
        if len(adjacent) >= size:
            shiftList(adjacent)
            
        adjacent.append(int(i))

        if len(adjacent) == size and findProduct(adjacent) > largest:
            largeList = adjacent
            largest = findProduct(largeList)
            print(largeList)

    print(largest)
