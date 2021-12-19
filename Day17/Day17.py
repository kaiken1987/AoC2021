import math

example = [range(20,30), range(-10,-4)]
input = [range(14,50), range(-267,-224)]#14..50, y=-267..-225
class Probe:
    target = []
    position=[0,0]
    velocity=[0,0]
    steps = 0
    maxY = 0
    def __init__(self, t, vx, vy) -> None:
        self.position=[0,0]
        self.velocity[0] = vx
        self.velocity[1] = vy
        self.target = t
        self.steps = 0

    def step(self) -> None:
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        if( self.velocity[0]>0):
            self.velocity[0] -= 1
        self.velocity[1] -= 1
        self.steps += 1

    def inTarget(self) -> bool:
        return self.position[0] in self.target[0] and self.position[1] in self.target[1]

    def failed(self) -> bool:
        return (self.position[0] > self.target[0].stop) or (self.position[1] < self.target[1].start)

    def run(self) -> bool:
        while( not self.failed() and not self.inTarget()):
            self.step()
            if self.position[1] > self.maxY:
                self.maxY = self.position[1]
        return self.inTarget()
        
    def __str__(self) -> str:
        result = f"Pos:{self.position} Vel:{self.velocity}"        
        return result
def checkNums(a,b) -> bool:
    return math.floor(a)==a or math.floor(b)==b or (math.floor(a)!=math.floor(b))

def part1():
    target = input#
    minTX = target[0].start
    #maxTY = target[1].start
    #maxVY = maxTY-target[1].start
    vx = math.floor( math.sqrt(minTX*2) )
    vy = 0#vx/2
    maxY = 0
    bestY = 0
    while True:
        vy += 1
        #solve using quadratic formula and y extents
        quad1 = vy*vy-2*target[1].start
        quad2 = vy*vy-2*target[1].stop
        if(quad1<0 or quad2<0):
            continue
        #look for integer of steps between min and max y of target
        t1 = (-vy - math.sqrt(quad1))/-1
        t2 = (-vy - math.sqrt(quad2))/-1
        if checkNums(t1,t2):
            p = Probe(target,vx,vy)
            if p.run() :
                bestY = vy
                maxY = p.maxY
        if t1-t2 <0.001: # this point it'll never span a integer value again
            break

    print( f"Part 1: {vx},{bestY}, Max Y: {maxY}")


def part2():
    print( "Part 2")

part1() 
part2() 