fname = "Day16\\Input.txt"
input = []
versSum = 0
hex2Bi = {	
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111",
}

def loadFile():
    f = open(fname, "r")
    for x in f:
        input.append(x.strip())

def expand( hex ):
    result = ""
    for c in hex:
        result += hex2Bi[c]
    return result

def getVal( line, lenght = -1 ):
    if lenght< 0 :
        lenght = len(line)
    while lenght>len(line) :
        line += '0'
    numStr = line[:lenght]
    line = line[lenght:]
    result = 0
    for b in numStr:
        result = result << 1
        if b == '1':
            result += 1
    return result, line
def literal( line ):
    result = 0
    nums = []
    while line[0] == '1' and len(line)>4:
        nums.append( line[1:5] )
        line = line[5:]
    if len(line)> 4:
        nums.append( line[1:5] )
        line = line[5:]
    for n in nums:
        for b in n:
            result = result << 1
            if b == '1':
                result += 1
    return result, line
    
def processModule(bits):
    global versSum
    vers, bits = getVal(bits, 3)
    versSum += vers
    type, bits = getVal(bits, 3)
    if type == 4:
        num, bits = literal(bits)
        return num, bits
    else: #operator
        nums = []
        if bits[0]== '0':
            lenSub, bits = getVal(bits[1:], 15)
            sub = bits[:lenSub]
            bits = bits[lenSub:]
            while( len(sub)>6 ):
                n, sub = processModule(sub)
                nums.append(n)                        
        else:
            numSub, bits = getVal(bits[1:], 11)
            for i in range(numSub):
                n, bits = processModule(bits)
                nums.append(n)
        result = 0
        if type == 0: #sum
            for n in nums:
                result += n
        elif type == 1: #product
            result = 1
            for n in nums:
                result *= n
        elif type == 2: #min
            result = nums[0]
            for n in nums:
                if n < result:
                    result = n
        elif type == 3: #max
            result = nums[0]
            for n in nums:
                if n > result:
                    result = n
        elif type == 5: #greater than
            if nums[0]>nums[1]:
                result = 1
        elif type == 6: #less than
            if nums[0]<nums[1]:
                result = 1
        elif type == 7: #equal to
            if nums[0]==nums[1]:
                result = 1
        return result, bits


def part1():
    global versSum
    loadFile()
    for line in input:
        versSum = 0
        bits = expand(line)
        nums, bits = processModule(bits)
        print( f"Part 1: {versSum}")
def part2():
    loadFile()
    for line in input:
        versSum = 0
        bits = expand(line)
        nums, bits = processModule(bits)
        print( f"Part 2 {nums}")

#part1() 
part2() 