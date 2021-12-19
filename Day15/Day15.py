import sys

nodes = []
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
   if y+1<len(input):
      result.append(input[y+1][x])
   if x>1:
      result.append(input[y][x-1])
   if x+1<len(input[y]):
      result.append(input[y][x+1])
   return result

def loadFile(part2 = False):
   f = open("Day15\\Input.txt", "r")
   nodes.clear()
   for x in f:
      x = x.strip()
      row = []
      for y in x:
         row.append(node(int(y)))
      if part2:
         wid = len(row)
         for i in range(1,5):
            for j in range(wid):
               v = row[j].value+i
               if v > 9: 
                  v-=9
               row.append(node(v))
      nodes.append(row)
   if part2:
      hei = len(nodes)
      for i in range(1,5):
         for j in range(hei):
            row = []
            for n in nodes[j]:
               v = n.value+i
               if v > 9: 
                  v-=9
               row.append(node(v))
            nodes.append(row)
   for y in range(len(nodes)):
      for x in range(len(nodes[y])):
         nodes[y][x].neighbors = getNeighbors(x,y,nodes)

class priorityQueue:
   queue = []
   def updateNode(self,node):
      idx = node.idx
      if(idx <1):
         return
      while( idx>0 and self[idx].dist<self[idx-1].dist):
         temp = self[idx]
         self[idx] = self[idx-1]
         self[idx-1] = temp
         self[idx-1].idx = idx-1
         self[idx].idx = idx
         idx -= 1
   def __getitem__(self,key):
      return self.queue[key]
   def __setitem__(self,key,value):
      self.queue[key] = value

   def popfront(self):
      result = self[0]
      for i in range(1,len(self.queue)):
         self[i].idx -= 1
         self[i-1] = self[i]
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
         Q.addNode(nodes[y][x])
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
    loadFile(True)
    risk = Dijkstra()
    print( f"Part 2: Risk:{risk}")

part1() 
#part2() 