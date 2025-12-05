# part 1
with open("5", 'r') as file:
    flag = 0
    fresh = 0
    ranges = set()
    ingridients = set()
    for line in file:
        if flag:
            ingridients.add(int(line[:-1]))
        else:
            if line == "\n":
                flag = 1
            else:
                r = line.split("-")
                ranges.add(range(int(r[0]), int(r[1][:-1])+1))
    for i in ingridients:
        l = [True if i in y else False for y in ranges]
        if any(l):
            fresh += 1
    print(fresh)

# part 2
with open("5", 'r') as file:
    fresh = 0
    ranges = []
    for line in file:
        if line == "\n":
            break
        else:
            r = line.split("-")
            ranges.append((int(r[0]), int(r[1][:-1])))
    ranges = sorted(ranges)
    combined = [ranges[0]]
    for r in ranges:
        if r[0] > combined[-1][1]:
            combined.append(r)
        else:
            if combined[-1][1] < r[1]:
                combined[-1] = (combined[-1][0], r[1])
    allids = 0
    for r in combined:
        allids += r[1] - r[0] + 1
    print(allids)
