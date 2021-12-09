f = open("Day8\\Input.txt", "r")

input =[]
output = []
for s in f:
   in_, out = s.strip().split(" | ", 2)
   input.append(in_.split())
   output.append(out.split())

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)   

def convertToBi(s):
   out = 0
   for l in char_range('a','g') :
      out = out<<1
      if s.count(l)>0:
         out += 1
   return out

def cntBits(x):
   cnt = 0
   for i in range(7):
      cnt += (x>>i)&1
   return cnt
def flagmatch( x, y ):
   return (x&y)==y
def part1():
   cnt = 0
   for i in range(len(output)):
      for p in output[i]:
         l = len(p)
         if(l==2)|(l==3)|(l==4)|(l==7):
            cnt += 1

   print( "Part 1: " + str(cnt) )
def part2():   
   for i in range(len(output)):
      encoding = [0,0,0,0,0,0,0,0,0,0]
      #convert input to bitflags and find the bit flags for 1,4,7,8
      for j in range(len(input[i])):
         input[i][j] = convertToBi(input[i][j])
         cnt = cntBits(input[i][j])
         #test for unqiue numbers (1,4,7,8)
         if cnt == 2:
            encoding[1] = input[i][j] 
         elif cnt == 3: 
            encoding[7] = input[i][j] 
         elif cnt == 4: 
            encoding[4] = input[i][j] 
         elif cnt == 7: 
            encoding[8] = input[i][j] 
      for j in range(len(output[i])):
         output[i][j] = convertToBi(output[i][j])
         cnt = cntBits(output[i][j])
         if cnt == 2:
            encoding[1] = output[i][j] 
         elif cnt == 3: 
            encoding[7] = output[i][j] 
         elif cnt == 4: 
            encoding[4] = output[i][j] 
         elif cnt == 7: 
            encoding[8] = output[i][j] 
      outvalue = 0      
      for j in range(len(output[i])):
         outvalue *= 10
         val = output[i][j]
         cnt = cntBits(output[i][j])
         if cnt == 6:
            if flagmatch(val, encoding[7]):
               if flagmatch(val, encoding[4]):
                  outvalue += 9
               else:
                  outvalue += 0
            else:
               outvalue += 6
         elif cnt == 5:
            if flagmatch(val, encoding[7]):
               outvalue += 3
            elif flagmatch(val, (encoding[4]-encoding[1])):
               outvalue += 5
            else:
               outvalue += 2
         elif cnt == 2:
            outvalue += 1
         elif cnt == 3: 
            outvalue += 7
         elif cnt == 4: 
            outvalue += 4
         elif cnt == 7: 
            outvalue += 8
      output[i] = outvalue
   sum = 0
   for v in output:
      sum += v
   print( "Part 2")
   print( output )
   print( sum )

part1() 
part2() 