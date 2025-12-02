# part 1
with open("2", 'r') as file:
    ranges = file.readline().split(",")
    summed = 0
    for rang in ranges:
        start, end = rang.split("-")
        for i in range(int(start), int(end) + 1):
            if len(str(i)) % 2 == 0 and str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                summed += i
    print(summed)

# part 2
with open("2", 'r') as file:
    ranges = file.readline().split(",")
    summed = 0
    for rang in ranges:
        start, end = rang.split("-")
        for i in range(int(start), int(end) + 1):
            i = str(i)
            if len(i) != 1:
                mods = [x for x in range(1, len(i) // 2 + 1) if len(i) % x == 0]
                if len(mods) != 1:
                    if len(set(i)) <= mods[-1]:
                        for m in mods:
                            parts = [i[ind:ind + len(i) // len(i)// m] for ind in range(0, len(i), len(i) // len(i)// m)]
                            s = set(p for p in parts)
                            if len(s) == 1:
                                summed += int(i)
                                break
                else:
                    s = set(i)
                    if len(s) == 1:
                        summed += int(i)
    print(summed)


