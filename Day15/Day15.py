import sys

nodes = []
graph = {}
class node:
   value = -1
   visited = False
   neighbors = []
   def __init__(self, v):
       self.value = v
def getNeighbors(x,y,input):
   result = []
   if y>1:
      result.append(input[y-1][x])
      #if x>1:
      #   result.append(input[y-1][x-1])
      #if x+1<len(input[y]):
      #   result.append(input[y-1][x+1])
   if y+1<len(input):
      result.append(input[y+1][x])
      #if x>1:
      #   result.append(input[y+1][x-1])
      #if x+1<len(input[y]):
      #   result.append(input[y+1][x+1])
   if x>1:
      result.append(input[y][x-1])
   if x+1<len(input[y]):
      result.append(input[y][x+1])
   return result

def loadFile():
   f = open("Day15\\Input.txt", "r")
   for x in f:
      x = x.strip()
      row = []
      for y in x:
         row.append(node(int(y)))
      nodes.append(row)

   for y in range(len(nodes)):
      for x in range(len(nodes[y])):
         nodes[y][x].neighbors = getNeighbors(x,y,nodes)


def Dijkstra():
   dist = []
   prev = []
   Q = []
   source = 0
   for y in range(len(nodes)):
      for x in range(len(nodes[y])):
         dist.append(2e30)
         prev.append(None)
         Q.append(nodes[y][x])
   target = Q[-1]
   dist[source] = 0
   curr = 0
   unvisted = len(Q)
   while unvisted>0:
      u = None
      d = 2e30
      best = -1
      for i in range(len(Q)):
         if not Q[i].visited and dist[i]<d:
            u = Q[i]
            d = dist[i]
            best = i
      if u == None: #all visted
         break
      u.visited = True
      unvisted -= 1
      for n in u.neighbors:
         i = Q.index(n)
         d2 = d+n.value
         if d2 < dist[i]:
            dist[i] = d2
            prev[i] = u
   return dist, prev


def part1():
    loadFile()
    dist, prev = Dijkstra()
    risk = dist[-1]
    print( f"Part 1: Risk:{risk}")

def part2():
    print( "Part 2")

part1() 
part2() 