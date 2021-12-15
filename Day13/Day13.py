
wid = 0
hei = 0
dots = []
folds = []
grid = []
def loadFile():
    global wid
    global hei
    #load dots
    f = open("Day13\\Input.txt", "r")
    for x in f:
        if x=="\n":
            break
        x = x.strip()
        dot = [int(y) for y in x.split(',')]
        if(dot[0]>=wid):
            wid = dot[0]+1
        if(dot[1]>=hei):
            hei = dot[1]+1
        dots.append(dot)
    #load folds
    for x in f:
        fold = [x[11],int(x.split("=",2)[1])]
        folds.append(fold)
def setupGrid():
    blankrow = []
    for x in range(wid):
        blankrow.append('.')
    for y in range (hei):
        grid.append(blankrow.copy())
    for d in dots:
        x = d[0]
        y = d[1]
        grid[y][x] = '#'
def printGrid():
    cnt = 0
    for row in grid:
        line = ""
        for c in row:
            line += c
            if( c=='#'):
                cnt += 1
        print(line)
    line = ""    
    for x in range(20):
        line += "--"
    print(line)
    return cnt
def foldGrid(fold):
    global grid
    global wid
    global hei
    newGrid = []
    if(fold[0]=='y'):
        for y in range(fold[1]):
            row = []
            y2 = fold[1]*2-y
            #init row
            for x in range(wid):
                if grid[y][x] == '#' or( (y2<hei) and (grid[y2][x] == '#') ):
                    row.append('#')
                else:
                    row.append('.')
            newGrid.append(row)
    elif(fold[0]=='x'):
        for y in range(hei):
            row = []
            for x in range(fold[1]):
                x2 = fold[1]*2-x
                if grid[y][x] == '#' or ( (x2<wid) and (grid[y][x2] == '#') ):
                    row.append('#')
                else:
                    row.append('.')
            newGrid.append(row)
    wid = len(newGrid[0])
    hei = len(newGrid)
    grid = newGrid

        


def part1():
    print( "Part 1")
    loadFile()
    setupGrid()
    printGrid()
    foldGrid(folds[0])
    result = printGrid()
    print( f"Dots Cnt: {result}")

def part2():
    print( "Part 2")
    loadFile()
    setupGrid()
    for f in folds:
        foldGrid(f)
    printGrid()

#part1() 
part2() 