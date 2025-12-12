with open("12", 'r') as file:
    gridFlag = False
    grids = []
    shapes = []
    shape = 0

    for i, line in enumerate(file):
        if gridFlag:
            s = line[:-1].split(":")
            g = [int(x) for x in s[0].split("x")]
            nums = [int(x) for x in s[1].split(" ")[1:]]
            grids.append((g[0],g[1], nums))
        else:
            if len(line) == 3:
                continue
            if len(line) == 1:
                shapes.append(shape)
                shape = 0
            else:
                s = sum([1 if x == "#" else 0 for x in line[:-1]])
                shape += s
            if i == 29:
                gridFlag = True

summed = 0
for x, y, nums in grids:
    allmatrixes = []
    slots = x * y
    for i, shape in enumerate(shapes):
        slots -= nums[i] * shapes[i]
    if slots > 0:
        summed += 1
print(summed)
