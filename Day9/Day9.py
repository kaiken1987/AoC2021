
grid = []
basins = []
width = 0
height = 0
def init():
   global width, height
   f = open("Day9\\Input.txt", "r")
   lines = []
   for x in f:
      lines.append(x.strip())

   height = len(lines)
   width = len(lines[0])
   #top border of 9s
   grid.append([])
   for c in range(width+2):
      grid[0].append(9)
   for r in range(height):
      grid.append([9])#left border of 9s
      for c in range(width):
         grid[r+1].append(int(lines[r][c]))
      grid[r+1].append(9)#right border of 9s
   #bottom border of 9s
   grid.append([])
   for c in range(width+2):
      grid[height+1].append(9)

def sizeBasin(x,y):
   if x < 1 or x>height or y>width or y<1 or grid[x][y]>=9:
      return 0
   else:
      grid[x][y] += 10
      left = sizeBasin(x-1,y)
      right = sizeBasin(x+1,y)
      top = sizeBasin(x,y+1)
      bottom = sizeBasin(x,y-1)
      return 1+left+right+top+bottom
      
      

def part1():
   print( "Part 1")
   init()
   sum = 0
   for r in grid:
      print(r)
   for x in range( 1, height+1):
      for y in range( 1, width+1):
         left = grid[x-1][y]
         right = grid[x+1][y]
         top = grid[x][y-1]
         bottom = grid[x][y+1]
         value = grid[x][y]
         if value < left and value<right and value<top and value<bottom:
            #print(value)
            basins.append([x,y])
            sum += value+1
   print(f"Answer: {sum}")

def part2():
   print( "Part 2")
   sizes = []
   result = 1
   for b in basins:
      x = b[0]
      y = b[1]
      sz = sizeBasin(x,y)
      sizes.append(sz)
      #print(sz)
      result *= sz
   sizes.sort()
   result = sizes[-1]*sizes[-2]*sizes[-3]
   print(sizes)
   print(f"Answer: {result}")
part1() 
part2() 