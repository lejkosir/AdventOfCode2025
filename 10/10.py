import heapq
from z3 import *

with open("10", 'r') as file:
    machines = []
    for line in file:
        s = line.split(" ")
        bit = [1 if x == "#" else 0 for x in s[0][1:-1]]
        buttons = [[int(a) for a in x.strip("()").split(",")] for x in s[1:-1]]
        joltage = [int(a) for a in s[-1][:-1].strip("{}").split(",")]
        machines.append([bit, buttons, joltage])
    summed = 0

def rec(machine, pq, visited):
    bit = machine[0]
    buttons = machine[1]
    while pq:
        presses, cur  = heapq.heappop(pq)
        if cur == bit:
            return presses
        for button in buttons:
            changes = cur[:]
            for idx in button:
                changes[idx] = 1 if changes[idx] == 0 else 0
            if tuple(changes) in visited:
                continue
            visited.add(tuple(changes))

            npresses = presses + 1
            heapq.heappush(pq, (npresses, changes))

# part 1, hotel A*, moral uporabiti djikstra
for machine in machines:
    pq = []
    bit = machine[0]
    current = [0 for _ in bit]
    buttons = machine[1]
    for button in buttons:
        changes = current[:]
        for idx in button:
            changes[idx] = 1 if changes[idx] == 0 else 0
        heapq.heappush(pq, (1, changes))
    summed += (rec(machine, pq, set()))
print(summed)

# part 2, Z3, resevanje kot vsota vektorjev
summed = 0
for machine in machines:
    opt = Optimize()
    buttons = machine[1]
    finstate = machine[2]
    newbuttons = [[1 if i in button else 0 for i in range(len(finstate))] for button in buttons]
    x = [Int(f'x{i}') for i in range(len(newbuttons))] # xi za vsak button
    spremembe = [Sum([x[i] * newbuttons[i][j] for i in range(len(newbuttons))]) for j in range(len(newbuttons[0]))] # vsak gumb kot vsota sprememb za vsako spremenljivko xi
    cons = [spremembe[i] == finstate[i] for i in range(len(finstate))] # iscemo za vsak i da je tolikokrat pritisnjen kot koncna vrednost
    opt.add(cons)
    opt.add([xi >= 0 for xi in x]) # ne moremo odstevati pritiskov
    opt.minimize(Sum(x))
    if opt.check() == sat:
        model = opt.model()
        r = [model.evaluate(xi).as_long() for xi in x]
        summed += sum(r)
print(summed)

