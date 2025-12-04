# part 1
with open("4", 'r') as file:
    grid = [[x for x in y[:-1]] for y in file]
    accasible = 0
    directions = [[x,y] for x in range(-1,2) for y in range(-1,2)]
    for y, line in enumerate(grid):
        for x, space in enumerate(line):
            if space == "@":
                adjacent = 0
                for direction in directions:
                    try:
                        if grid[y+direction[1]][x+direction[0]] == "@" and x+direction[0] >= 0 and y+direction[1] >= 0:
                            adjacent += 1
                            if adjacent > 4:
                                break
                    except IndexError:
                        continue
                if adjacent <= 4:
                    accasible += 1
    print(accasible)

# part 2, samo dodan while loop :)
with open("4", 'r') as file:
    grid = [[x for x in y[:-1]] for y in file]
    accasible = 0
    directions = [[x,y] for x in range(-1,2) for y in range(-1,2)]
    while True:
        removed = 0
        for y, line in enumerate(grid):
            for x, space in enumerate(line):
                if space == "@":
                    adjacent = 0
                    for direction in directions:
                        try:
                            if grid[y+direction[1]][x+direction[0]] == "@" and x+direction[0] >= 0 and y+direction[1] >= 0:
                                adjacent += 1
                                if adjacent > 4:
                                    break
                        except IndexError:
                            continue
                    if adjacent <= 4:
                        accasible += 1
                        removed += 1
                        grid[y][x] = "."
        if not removed:
            break
    print(accasible)

