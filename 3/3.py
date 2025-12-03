# part 1
with open("3", 'r') as file:
    summed = 0
    for line in file:
        largest = ""
        linelist = [int(x) for x in line[:-1]]
        for i in range(2):
            dol = len(linelist) - (2-i)
            largestinex = linelist.index(max(linelist[:dol+1]))
            largest += str(linelist[largestinex])
            linelist = linelist[largestinex+1:]
        summed += int(largest)
    print(summed)

# part 2
with open("3", 'r') as file:
    summed = 0
    for line in file:
        largest = ""
        linelist = [int(x) for x in line[:-1]]
        for i in range(12):
            dol = len(linelist) - (12-i)
            largestinex = linelist.index(max(linelist[:dol+1]))
            largest += str(linelist[largestinex])
            linelist = linelist[largestinex+1:]
        summed += int(largest)
    print(summed)









