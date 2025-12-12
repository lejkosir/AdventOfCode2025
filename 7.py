# part 1
with open("7", 'r') as file:
    twod = []
    splited = 0
    for line in file:
        twod.append([x for x in line[:-1]])
    for x, c in enumerate(twod[0]):
        if c == "S":
            twod[1][x] = "|"
    for y, line in enumerate(twod):
        if y == 0:
            for x, c in enumerate(line):
                if c == "S":
                    twod[1][x] = "|"
        else:
            try:
                for x, c in enumerate(line):
                    if c == "|":
                        if twod[y+1][x] == "^":
                            splited += 1
                            twod[y+1][x-1] = "|"
                            twod[y+1][x+1] = "|"
                        else:
                            twod[y+1][x] = "|"
            except IndexError:
                ...
    print(splited)

# part 2
def findown(y,x,twod):
    down = []
    for i in range(y, len(twod)-1):
        if twod[i][x+1] == "^":
            down.append((i,x+1))
            break
    for i in range(y, len(twod) - 1):
        if twod[i][x-1] == "^":
            down.append((i,x-1))
            break
    return down

with open("7", 'r') as file:
    twod = []
    splited = 0
    downward = {}
    last = ()
    for line in file:
        twod.append([x for x in line[:-1]])
    for y in range(len(twod)-2, 0, -2):
        for x in range(len(twod[0])-1, 0, -1):
            if twod[y][x] == "^":
                last = (y,x)
                downward[(y,x)] = 0
                d = findown(y,x,twod)
                for dd in d:
                    downward[(y, x)] += downward[dd]
                downward[(y, x)] += 2-len(d)
    print(downward[last])