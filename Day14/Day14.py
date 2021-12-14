import math
template = []
inserts = {}

def loadInput():
    global template
    f = open("Day14\\Input.txt", "r")
    input = f.readline().strip()
    template = []
    for x in input:
        template.append(x)
    f.readline()
    for x in f:
        a,b = x.strip().split(" -> ",2)
        inserts[a] = b

def iterate(input):
    result = []
    for i in range(len(input)-1):
        a = input[i]
        b = input[i+1]
        ab = a+b
        result.append(a)
        c = inserts[ab]
        if c:
            result .append(c)
    result += input[-1]
    return result 

def part1():
    global template
    loadInput()
    for i in range(10):
        template = iterate(template)
        #print( f"after step {i+1}: {template}")
    elements = {}
    for i in range(len(template)):
        a = template[i]
        if a not in elements:
            elements[a] = 1
        else:
            elements[a] += 1
    min = len(template)
    max = 0
    for x in elements:
        x = elements[x]
        if x<min:
            min = x
        if x>max:
            max = x
    print( f"Part 1: {max-min}")

def incPair( pairs, ab, cnt=1):
    if ab in pairs:
        pairs[ab] += cnt
    else:
        pairs[ab] = cnt

def part2():
    global template
    global inserts
    maxDepth = 40
    pairCnt = {}
    elements = {}
    loadInput()
    for i in range(len(template)-1):
        ab = template[i] + template[i+1]
        incPair( pairCnt, ab)
    for i in range(maxDepth):
        newPairs = {}
        for x in pairCnt:
            a,b = x
            c = inserts[x]
            cnt = pairCnt[x]
            incPair(newPairs,a+c, cnt)
            incPair(newPairs,c+b, cnt)
        pairCnt = newPairs
    for x in pairCnt:
        cnt = pairCnt[x]
        a,b = x
        if a in elements:
            elements[a] += cnt
        else:
            elements[a] = cnt
    elements[template[-1]] += 1

    min = 2e30
    max = 0
    for x in elements:
        x = elements[x]
        if x<min:
            min = x
        if x>max:
            max = x
    print( f"Part 2: {max-min}")

part1() 
part2() 