# part 1
with open("9", 'r') as file:
    tiles = []
    for line in file:
        s = line.split(",")
        tiles.append((int(s[0]),int(s[1])))
    tiles = sorted(tiles, key=lambda x: x[1])
    height = tiles[-1][1] - tiles[0][1]
    biggest = 0
    for i, tile in enumerate(tiles):
        for j, tile2 in enumerate(tiles[i:]):
            size = ((max(tile2[0], tile[0]) - min(tile2[0], tile[0])) + 1) * ((max(tile2[1], tile[1]) - min(tile2[1], tile[1])) + 1)
            if size > biggest:
                biggest = size
    print(biggest)

# part 2, traja par minut ampak dela...
with open("9", 'r') as file:
    tiles = []
    green = set()
    outside = set()
    for line in file:
        s = line.split(",")
        tiles.append((int(s[0]),int(s[1])))

    print("drawing lines")
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % len(tiles)]
        dx, dy = x2 - x1, y2 - y1
        direction = [dx // abs(dx) if dx != 0 else 0, dy // abs(dy) if dy != 0 else 0]
        left = (direction[1], -direction[0])

        steps = abs(dx) if dx != 0 else abs(dy)
        for j in range(steps + 1):
            x = x1 + j * direction[0]
            y = y1 + j * direction[1]
            green.add((x, y))
            outside.add((x + left[0], y + left[1]))
    outside -= green
    tiles = sorted(tiles, key=lambda x: x[1])
    height = tiles[-1][1] - tiles[0][1]
    biggest = 0
    print("checking")
    for i, tile in enumerate(tiles):
        print(i, biggest)
        for tile2 in tiles[i:]:
            x1, y1 = tile
            x2, y2 = tile2

            xmin, xmax = sorted([x1, x2])
            ymin, ymax = sorted([y1, y2])
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            if area < biggest:
                continue
            flag = False
            for y in range(ymin + 1, ymax):
                if (xmin, y) in outside or (xmax, y) in outside:
                    flag = True
                    break
            if flag:
                continue

            for x in range(xmin + 1, xmax):
                if (x, ymin) in outside or (x, ymax) in outside:
                    flag = True
                    break
            if flag:
                continue

            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            if area > biggest:
                biggest = area
    print(biggest)
