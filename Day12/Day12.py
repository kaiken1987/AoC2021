f = open("Day12\\Input.txt", "r")

map = {}

routes = []

def addPath(a,b):
    if a not in map:
        map[a] = []
    if b not in map:
        map[b] = []
    map[a].append(b)
    map[b].append(a)
def isSmall(cave):
    return cave.lower() == cave
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

def part1():
    print( "Part 1")
    findPath("start", [], True )
    for r in routes:
        print(r)
    print( f"{len(routes)} possible paths")
def part2():
    print( "Part 2")
    routes.clear()
    findPath("start", [], False )
    #routes.sort()
    #for r in routes:
    #    print(r)
    print( f"{len(routes)} possible paths")

loadMap()
#part1() 
part2() 