f = open("Day2\\Input.txt", "r")

def part1():
    dist = 0
    depth = 0
    for x in f:
        cmd, val = x.split(" ", 1)
        val = int(val)
        if cmd == "forward":
            dist = dist + val
        if cmd == "down":
            depth = depth + int(val)
        if cmd == "up":
            depth = depth - int(val)
    print( "Final Position " + str(dist) + ", " + str(depth) + " x*y: " + str(dist*depth) )
    
def part2():
    dist = 0
    depth = 0
    aim = 0
    for x in f:
        cmd, val = x.split(" ", 1)
        val = int(val)
        if cmd == "forward":
            dist = dist + val
            depth = depth + (aim*val)
        if cmd == "down":
            aim = aim + val
        if cmd == "up":
            aim = aim - val
    print( "Final Position " + str(dist) + ", " + str(depth) + " x*y: " + str(dist*depth) )

part2() 