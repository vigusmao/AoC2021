from heapq import heapify, heappush, heappop
from time import time


X = 0
Y = 1

def neighbors(x, y, rows, cols):
    result = []
    if x > 0:
        result.append((x - 1, y))
    if x < cols - 1:
        result.append((x + 1, y))
    if y > 0:
        result.append((x, y - 1))
    if y < rows - 1:
        result.append((x, y + 1))
    return result


def get_cost(node, costs):
    return int(costs[node[Y]][node[X]])


def shortest_path(x, y, rows, cols, costs):
    estimates = [(0, (x, y))]
    marked_nodes = set()
    cost_by_node = {(x, y): 0}
    target = (cols - 1, rows - 1)

    while target not in marked_nodes:
        heap_entry = heappop(estimates)

        node = heap_entry[1]
        if node in marked_nodes:
            continue

        cost = heap_entry[0]
        marked_nodes.add(node)
        cost_by_node[node] = cost

        for neighbor in neighbors(node[X], node[Y], rows, cols):
            if neighbor not in marked_nodes:
                heappush(estimates, (cost + get_cost(neighbor, costs), neighbor))

    return cost_by_node.get(target)


def process(lines):
    costs = []
    for line in lines:
        if len(line) == 0:
            continue
        row = line
        previous_part = line
        for tile_col in range(1, 5):
            next_part = ''.join([str(int(x) + 1) if int(x) < 9 else '1' for x in previous_part])
            row += next_part
            previous_part = next_part
        costs.append(row)

    previous_rows = costs[:]

    for tile_row in range(1, 5):
        next_rows = []
        for row in previous_rows:
            next_row = ''.join([str(int(x) + 1) if int(x) < 9 else '1' for x in row])
            next_rows.append(next_row)
        previous_rows = next_rows
        costs += next_rows

    rows = len(costs)
    cols = len(costs[0])

    return shortest_path(0, 0, rows, cols, costs)


with open("/Users/viniciusgusmao/Documents/AoC2021/15.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    start = time()
    result = process(lines)
    duration = time() - start
    print result
    print "%.6f" % duration
