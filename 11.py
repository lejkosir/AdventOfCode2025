def dfs(cur, visited, out, cache):
    key = (cur, out)
    if key in cache:
        return cache[key]
    if cur in visited:
        return 0
    if cur == out:
        return 1
    if cur == "out":
        return 0
    new_visited = visited + (cur,)
    tot = 0
    for node in graph[cur]:
        tot += dfs(node, new_visited, out, cache)
    cache[key] = tot
    return tot

# srv -> dac/fft -> fft/dac -> out
# srv dac fft out / srv fft dac out, kombinatorika :)
with open("11", 'r') as file:
    graph = {}
    for line in file:
        line = line.rstrip().split(":")
        s = line[1].split(" ")
        graph[line[0]] = s[1:]
    print("part 1: " + str(dfs("you", tuple(), "out", {})))
    cache = {}
    svrdac = dfs("svr", tuple(), "dac", cache)
    dacfft = dfs("dac", tuple(), "fft", cache)
    fftout = dfs("fft", tuple(), "out", cache)
    svrfft = dfs("svr", tuple(), "fft", cache)
    fftdac = dfs("fft", tuple(), "dac", cache)
    dacout = dfs("dac", tuple(), "out", cache)

    print("part 2: " + str(svrdac * dacfft * fftout + svrfft * fftdac * dacout))