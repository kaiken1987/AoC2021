f = open("Day12\\Input.txt", "r")

map = {}
routes = []
visitCount = {}
foundRts = 0

def isSmall(cave):
    return cave.lower() == cave
def addPath(a,b):
    if a not in map:
        map[a] = []
        if isSmall(a):
            visitCount[a] = 0
        else:
            visitCount[a] = -1
    if b not in map:
        map[b] = []
        if isSmall(b):
            visitCount[b] = 0
        else:
            visitCount[b] = -1
    map[a].append(b)
    map[b].append(a)

def loadMap():
    for l in f:
        path = l.strip().split('-')
        addPath(path[0],path[1])
def findPath(cur,soFar, smallLimit):
    soFar.append(cur)
    for cave in map[cur]:
        if cave == "start":
            continue
        if cave == "end":
            end = soFar.copy()
            end.append(cave)
            if not (end in routes):
                routes.append(end)
        elif isSmall(cave):
            visits = soFar.count(cave)
            if visits==1 and not smallLimit:
                findPath(cave, soFar.copy(), True)
            elif visits == 0:
                findPath(cave, soFar.copy(), smallLimit)            
        else: #bigCaves
            findPath(cave, soFar.copy(), smallLimit)

def findPath2(cur, visCnt, smallLimit):
    global foundRts
    for cave in map[cur]:
        cnt = visCnt[cave]
        if cave == "start":
            continue
        elif cave == "end":
            foundRts += 1
        elif cnt<0: #big cave
            findPath2(cave, visCnt, smallLimit)
        elif cnt == 0: #small unvisited cave
            new = visCnt.copy()
            new[cave] = 1
            findPath2(cave, new, smallLimit)
        elif not smallLimit: #caves visited once before
            findPath2(cave, visCnt, True)
def part1():
    print( "Part 1")
    findPath("start", [], True )
    for r in routes:
        print(r)
    print( f"{len(routes)} possible paths")
def part2():
    print( "Part 2")
    findPath2("start", visitCount, False ) #Too slow need a better way
    print( f"{foundRts} possible paths")

loadMap()
#part1() 
part2() 