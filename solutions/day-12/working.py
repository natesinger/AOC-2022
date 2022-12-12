from heapq import heapify, heappop, heappush

adj = lambda g, x, y : (z for z in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)) if z in g and order.index(g[z]) - order.index(g[x,y]) <= 1)
adj2 = lambda g, x, y : (z for z in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)) if z in g and order.index(g[x,y]) - order.index(g[z]) <= 1)

def path_finder(grid, start, end, p2=False):
    ad = adj if not p2 else adj2
    best_dict = {start : 0}
    queue = [(0, start)]
    heapify(queue)
    while queue:
        steps, (x,y) = heappop(queue)
        if ((x,y) == end if not p2 else grid[x,y] == "a"):
            return steps
        next_steps = steps + 1
        for a,b in ad(grid, x, y):
            if (current := best_dict.get((a,b), None)) is not None:
                if current <= next_steps:
                    continue
            best_dict[a,b] = next_steps
            heappush(queue, [next_steps, (a,b)])


with open("input.txt", "r") as file:
    data = file.read().splitlines()
    order = [chr(x) for x in range(97, 123)] + [chr(x) for x in range(65, 91)]
    grid = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (char := data[y][x]) == "E":
                end, char = (x,y), "z"
            elif char == "S":
                start, char = (x,y), "a"
            grid[x,y] = char
    print("day 12: ", path_finder(grid, start, end), path_finder(grid, end, start, p2=True))