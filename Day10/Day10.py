f = open("Day10\\Input.txt", "r")

def part1():
    print( "Part 1")
    stack = []#{'(':0,'[':0,'{':0,'<':0}
    open = {'(':')','[':']','{':'}','<':'>'}
    #close = {')':'(',']':'[','}':'{','>':'<'}
    errors = {')':0,']':0,'}':0,'>':0}
    for line in f:
        line = line.strip()
        for c in line:
            if c in ['(','[','{','<']:
                stack.append(c)
            else:
                #c = close[c]
                o = open[stack.pop()]
                if o != c:                    
                    errors[c] += 1
                    break
    print(errors)
    sum = errors[')']*3+errors[']']*57+errors['}']*1197+errors['>']*25137
    print( f"Anser: {sum}")

def part2():
    print( "Part 2")

part1() 
part2() 