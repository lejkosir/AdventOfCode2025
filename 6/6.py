# part 1
with open("6", 'r') as file:
    grand = 0
    problems = []
    for ind, line in enumerate(file):
        line = list(filter(None, line[:-1].split(" ")))
        for i, num in enumerate(line):
            if ind == 0:
                problems += [[num]]
            else:
                problems[i].append(num)
    for problem in problems:
        summed = int(problem[0])
        op = 1 if problem[-1] == "*" else 0
        for num in problem[1:-1]:
            if op == 1:
                summed *= int(num)
            else:
                summed += int(num)
        grand += summed
    print(grand)

# part 2, najgrsa stvar na svetu
with open("6", 'r') as file:
    grand = 0
    plenghts = []
    problems = []
    for ind, line in enumerate(file):
        if ind == 4:
            l = 1
            for char in line[1:-1]:
                if char == "*" or char == "+":
                    plenghts.append(l-1)
                    l = 1
                else:
                    l += 1
        else:
            pass
    plenghts.append(2)
with open("6", 'r') as file:
    for ind, line in enumerate(file):
        i = 0
        for j, plen in enumerate(plenghts):
            if ind == 0:
                problems += [[line[i:i+plen]]]
                i += plen + 1
            else:
                problems[j].append(line[i:i+plen])
                i += plen + 1
    reformat = [[] for _ in range(len(problems))]
    for i, problem in enumerate(problems):
        for j, p in enumerate(problem):
            reformat[i].append([])
        for j in range(plenghts[i]):
            for n, x in enumerate(problem):
                if n != 4:
                    reformat[i][n].append(x[j])
                else:
                    reformat[i][4].append(x[0])
    actualreformat = []
    for problem in reformat:
        result = [''.join(group) for group in zip(*problem[:-1])]
        result.append(problem[-1][0])
        actualreformat.append(result)
    grand = 0
    for problem in actualreformat:
        summed = int(problem[0])
        op = 1 if problem[-1] == "*" else 0
        for num in problem[1:-1]:
            if op == 1:
                summed *= int(num)
            else:
                summed += int(num)
        grand += summed
    print(grand)

