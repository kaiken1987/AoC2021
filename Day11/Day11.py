f = open("Day11\\Input.txt", "r")

#load data
octs = []
for l in f:
    l = l.strip()
    row = [int(x) for x in l]
    octs.append(row)

def incOct(y,x):
    if x<0 or y<0:
        return
    elif y>=len(octs) or x>=len(octs[y]):
        return
    elif octs[y][x]<=9: #only flash if haven't flashed already
        octs[y][x] += 1     
        if( octs[y][x]>9 ):
            for x1 in range(x-1,x+2): 
                incOct(y-1, x1)#above
                incOct(y+1, x1)#below
            incOct(y, x-1)#left
            incOct(y, x+1)#right

def step():
    flashes = 0
    for y in range(len(octs)):
        for x in range(len(octs[y])):
            incOct(y,x)
    #reset if flashed
    for y in range(len(octs)):
        for x in range(len(octs[y])):
            if octs[y][x]>9 :
                octs[y][x] = 0
                flashes += 1
    return flashes 


def part1():
    print( "Part 1")
    flashed = 0
    for i in range(100):
        flashed += step()
    print(f"Flashes: {flashed}")
def part2():
    print( "Part 2")
    flashed = 0
    while True:
        flashed += 1 
        if( step()== 100):
            break
    print(f"Flashes: {flashed}")

part2() 