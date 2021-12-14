
template = ""
inserts = {}


def loadInput():
    global template
    f = open("Day14\\TestInput.txt", "r")
    template = f.readline().strip()
    f.readline()
    for x in f:
        a,b = x.strip().split(" -> ",2)
        inserts[a] = b    
def iterate(input):
    result = ""
    for i in range(len(input)-1):
        a = input[i]
        b = input[i+1]
        ab = a+b
        c = inserts[ab]
        if c:
            result += a+c
        else:
            result += a
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
    
def part2():
    print( f"Part 2")

part1() 
part2() 