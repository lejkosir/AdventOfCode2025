import math
from collections import defaultdict
from itertools import combinations

def euclidian(j1, j2):
    return math.sqrt((j1[0]-j2[0])**2+(j1[1]-j2[1])**2 +(j1[2]-j2[2])**2)

# part 1 & 2
with open("8", 'r') as file:
    d = {}
    l = []
    for line in file:
        s = tuple(int(x) for x in line.split(","))
        d[s] = 0
        l.append(s)
    counter = 1
    connected = set()
    dolzine = []
    for x, y in combinations(l, 2):
        dist = euclidian(x, y)
        dolzine.append((dist, x, y))
    dolzine.sort()
    c = 0
    while any(v == 0 for v in d.values()):
        if c == 999:
            grouped = defaultdict(list)
            for key, value in d.items():
                grouped[value].append(key)
            sort = dict(sorted(grouped.items(), key=lambda item: len(item[1]), reverse=True))
            dol = [len(v) for v in list(sort.values())[1:4]]
            print(dol[0] * dol[1] * dol[2])
        for dist, a, b in dolzine:
            if (a, b) not in connected and (b, a) not in connected:
                par = (a, b)
                break
        if d[par[1]] == 0 and d[par[0]] == 0:
            d[par[1]] = counter
            d[par[0]] = counter
            counter += 1
        elif d[par[1]] == 0 and d[par[0]] != 0:
            d[par[1]] = d[par[0]]
        elif d[par[1]] != 0 and d[par[0]] == 0:
            d[par[0]] = d[par[1]]
        elif d[par[1]] != 0 and d[par[0]] != 0 and d[par[1]] != d[par[0]]:
            old = d[par[1]]
            new = d[par[0]]
            for key in d:
                if d[key] == old:
                    d[key] = new
        connected.add(par)
        c+=1
    print(par[0][0] * par[1][0])
