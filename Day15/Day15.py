input = []
graph = {}

def getNeighbors(x,y,input):
   result = []
   for x1 in range(x-1,x+1):
      result.append([x1,y-1])
      result.append([x1,y+1])
   result.append([x-1,y])
   result.append([x+1,y])
   for a in result:
      if(a[1]<0 or a[1]>=len(input)):
         result.remove(a)
      elif(a[0]<0 or a[0]>=len(input[a[1]])):
         result.remove(a)
    return result

def loadFile():
   f = open("Day15\\TestInput.txt", "r")
   for x in f:
      input.append([int(y) for y in x])

   for y in range(len(input)):
      for x in range(len(input[y])):
         neigh = getNeighbors(x,y,input)
         graph[input[y][x]] = neigh


def Dijkstra():
   dist = []
   prev = []
   Q = []
   for y in range(len(input)):
      for x in range(len(input[y])):
         dist.append(2e30)
         prev.append(None)
         Q.append(input[y][x])
   dist[0] = 0

   while len(Q)>0:
      u = Q[0]
      Q.remove(u)
      neigh = getNeighbors(u[0],u[1],input)
      for 


def part1():
    print( "Part 1")
def part2():
    print( "Part 2")

part1() 
part2() 