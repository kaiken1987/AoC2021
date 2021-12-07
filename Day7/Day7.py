f = open("Input.txt", "r")

positions = [int(x) for x in f.readline().split(",")]

maxPos = 0
for p in positions:
   if p>maxPos:
      maxPos = p

def part1():
   print( "Part 1")
   bestp = 0
   bestdis = maxPos*len(positions)
   for x in range(maxPos):
      dist = 0
      for p in positions:
         dist += abs(p-x)
      if(dist<bestdis):
         bestdis = dist
         bestp = x         
   print( "Best Pos: " + str( bestp ) + " Fuel: " + str(bestdis) )

def part2():
   print( "Part 2")
   bestp = 0
   bestdis = maxPos*maxPos*len(positions)
   for x in range(maxPos):
      dist = 0
      for p in positions:
         d = abs(p-x)
         d = d*(d+1)/2
         dist += d
      if(dist<bestdis):
         bestdis = dist
         bestp = x
   print( "Best Pos: " + str( bestp ) + " Fuel: " + str(bestdis) )
#part1() 
part2() 