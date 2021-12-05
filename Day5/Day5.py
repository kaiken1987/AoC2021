
lines = []
grid = []
maxx = 1
maxy = 1

def loadLines( straight = True):
    f = open("Day5\\Input.txt", "r")
    global maxx, maxy
    maxx = 1
    maxy = 1
    lines.clear()
    for s in f:
        pts = s.split(" -> ", 2)
        for i in range(len(pts)):
            pts[i] = pts[i].split(",",2)
            pts[i][0] = int(pts[i][0])
            pts[i][1] = int(pts[i][1])
            maxx = max(maxx,pts[i][0])
            maxy = max(maxy,pts[i][1])
        if straight & ( (pts[0][0]==pts[1][0]) | (pts[0][1]==pts[1][1]) ):
            lines.append(pts)
        elif not straight:
            lines.append(pts)
    grid.clear
    for x in range(maxx+1):
        row =[]
        for y in range(maxy+1):
            row.append(0)
        if x < len(grid):
            grid[x] = row
        else:
            grid.append(row)

def visitLine(p1,p2):
    if (p1[0]==p2[0]) | (p1[1]==p2[1]):
        for y in range(p1[1],p2[1]+1):
            for x in range(p1[0],p2[0]+1):
                grid[x][y] += 1 #visit point
    else:
        sx = p1[0]
        sy = p1[1]
        ex = p2[0]
        ey = p2[1]
        d = abs(ex-sx)
        dx = int((ex-sx)/d)
        dy = int((ey-sy)/d)
        for i in range(d+1):
            grid[sx+dx*i][sy+dy*i] += 1

def part1():
    loadLines(True)
    print( "Part 1")
    for l in lines:
        l.sort()
        visitLine(l[0],l[1])
    overlap = 0
    for r in grid:
        for c in r:
            if c>1:
                overlap += 1
    print( "Overlap: " + str(overlap))
def part2():
    print( "Part 2")
    loadLines(False)
    for l in lines:
        l.sort()
        visitLine(l[0],l[1])
    overlap = 0
    for r in grid:
        #print( r )
        for c in r:
            if c>1:
                overlap += 1
    print( "Overlap: " + str(overlap))

part1() 
part2() 