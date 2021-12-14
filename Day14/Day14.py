import math
template = []
inserts = {}
elements = {}

def tobitFlags(str):
    result = 0
    for x in str:
        result += (1<<(ord(x)-ord('A')))
    return str

def loadInput():
    global template
    f = open("Day14\\TestInput.txt", "r")
    input = f.readline().strip()
    template = []
    for x in input:
        template.append(tobitFlags(x))
    f.readline()
    for x in f:
        a,b = x.strip().split(" -> ",2)
        a = tobitFlags(a)
        b = tobitFlags(b)
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

def process( a, b, maxDep):
    global elements
    global inserts
    ab = a+b
    c = inserts[ab]
    if c not in elements:
        elements[c] = 1
    else:
        elements[c] += 1
    if maxDep>1:
        process(a,c, maxDep-1)
        process(c,b, maxDep-1)

def part1():
    global template
    global elements
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

def part2():
    global template
    global elements
    global inserts
    maxDepth = 40
    elements = {}
    loadInput()
    #for x in range(26):
    #    x = chr(x+ord('A'))
    #    elements[x] = 0
    for c in template:
        elements[c] = 1
    for i in range(len(template)-1):
        process(template[i], template[i+1], maxDepth)
    min = 2e30
    max = 0
    counts = {}
    for k in elements:
        x = elements[k]
        if x<min and x>0:
            min = x
        if x>max:
            max = x

    print( f"Part 2: {max-min}")

part1() 
part2() 