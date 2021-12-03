from collections import Counter

f = open("Day3\\Input.txt", "r")

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
    for s in f:
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
def part2():
    print( "Part 2")

part1()