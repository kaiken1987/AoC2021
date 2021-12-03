
def part1():
    f = open("Day1\\Input.txt", "r")
    count = 0
    prev = -1
    for x in f:
        curr = int(x)
        if (prev > 0) & (curr>prev): 
            count = count + 1
        prev = curr
        
    print( 'Number incr ' + str( count ) )


def part2():
    f = open("Day1\\Input.txt", "r")
    count = 0
    prev1 = -1
    prev2 = -1
    prev3 = -1
    for x in f:
        curr = int(x)
        if (prev1 > 0) & (curr>prev1): 
            count = count + 1
        prev1 = prev2
        prev2 = prev3
        prev3 = curr
        
    print( 'Number incr ' + str( count ) )

part1()
part2()