import sys

nodes = []
graph = {}
class node:
   value = -1
   visited = False
   dist = 2e30
   prev = None
   idx = -1
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

class priorityQueue:
   queue = []
   def updateNode(self,node):
      idx = node.idx
      if(idx <0):
         return
      while( idx>0 and self.queue[idx].dist>self.queue[idx-1].dist):
         temp = self.queue[idx]
         self.queue[idx] = self.queue[idx-1]
         self.queue[idx-1] = temp
         self.queue[idx-1].idx = idx-1
         self.queue[idx].idx = idx
         idx -= 1

   def popfront(self):
      result = self.queue[0]
      for i in range(1,len(self.queue)):
         self.queue[i-1] = self.queue[i]
      self.queue.pop()
      result.idx = -1
      return result

   def addNode(self, node):
      node.idx = len(self.queue)
      self.queue.append(node)



def Dijkstra():
   Q = priorityQueue()
   source = 0
   for y in range(len(nodes)):
      for x in range(len(nodes[y])):
         Q.queue.append(nodes[y][x])
   target = Q.queue[-1]
   Q.queue[0].dist = 0
   curr = 0
   unvisted = len(Q.queue)
   while len(Q.queue)>0:
      u = Q.popfront()
      if u == target:
         break
      unvisted -= 1
      for n in u.neighbors:
         d2 = u.dist+n.value
         if d2 < n.dist:
            n.dist = d2
            n.prev = u
            Q.updateNode(n)
   return target.dist


def part1():
    loadFile()
    risk = Dijkstra()
    print( f"Part 1: Risk:{risk}")

def part2():
    print( "Part 2")

part1() 
part2() 