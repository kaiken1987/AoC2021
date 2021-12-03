from collections import Counter

f = open("Day3\\Input.txt", "r")
vals = []
for s in f:
    vals.append(s.strip())

def bi2int( s = "11111" ):
    val = 0
    r = len(s)
    for i in range( r ):
        if s[i] == '1':
            val += pow(2,(r-i-1))
    return val

def arrTobi( arr ):
    bi = ""
    for i in range(len(arr)):
        if arr[i]<0:
            bi += '0'
        elif arr[i]>0:
            bi += '1'
    return bi

def invertArr( arr ):
    for i in range(len(arr)):
        arr[i] = -arr[i]

def part1():
    commons = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for s in vals:
        for i in range(len(s)):
            c = s[i]
            if c == '0':
                commons[i] -= 1
            if c == '1':
                commons[i] += 1

    gammaStr = arrTobi( commons )
    gamma = bi2int( gammaStr )     
    invertArr( commons )
    epsilonStr = arrTobi( commons )
    epsilon = bi2int( epsilonStr )            
    

    print( "Power Consumption: " + str(gamma*epsilon) )
def part2(vals, least = False):
    l = len( vals[0])
    for i in range(l):
        common = 0
        for s in vals:
            c = s[i]
            if c == '0':
                common -= 1
            if c == '1':
                common += 1
        if least:
            common *= -1
            if common == 0:
                common -= 1
        newvals = []
        for j in range(len(vals)):
            s = vals[j]
            c = s[i]
            if ((c == '0') & (common<0) ) | ((c == '1') & (common>=0)):
                newvals.append(s)
        vals = newvals
        if len(newvals) <= 1:
            v = bi2int(vals[0])
            print("last val: " + str(v))
            return v


part1()
o2 = vals
co2 = vals
o2 = part2(o2)
co2 = part2(co2, True)
print( "Part 2: " + str(o2*co2))