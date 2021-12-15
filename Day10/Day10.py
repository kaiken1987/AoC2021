f = open("Day10\\Input.txt", "r")
valid = []
def day10():
    #part 1 stuff
    open = {'(':')','[':']','{':'}','<':'>'} #convert open chars to close chars
    errors = {')':0,']':0,'}':0,'>':0} # count of illegal char for answer
    #part 2
    scoring = {')':1,']':2,'}':3,'>':4}
    autoScores = [] #list of scores for auto complete
    for line in f:
        line = line.strip()
        error = False
        stack = [] #unclosed chunk stack
        #part1 find mis matched closes
        for c in line:
            if c in ['(','[','{','<']:
                stack.append(c) #open chunk
            else: #close chunk
                o = open[stack.pop()]
                if o != c:    #found c expect o to close chunk
                    errors[c] += 1
                    error = True #error found skip line for part 2
                    break
        if  error:
            continue
        #part2 auto complete line
        score = 0
        while len(stack)>0:
            score *= 5
            c = open[stack.pop()]
            score += scoring[c]
        autoScores.append(score)
    print( "Part 1")
    print(errors)
    sum = errors[')']*3+errors[']']*57+errors['}']*1197+errors['>']*25137
    print( f"Anser: {sum}")

    print( "Part 2")
    autoScores.sort()
    mid = int(len(autoScores)/2)
    mid = autoScores[mid]
    print( f"Anser: {mid}")

day10() 