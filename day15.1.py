memo = {}


def solve(x, y, rows, cols, costs):
    memoized_result = memo.get((x, y))
    if memoized_result is not None:
        return memoized_result

    try:
        result = int(costs[y][x])
    except Exception:
        x = 1

    if x == cols - 1 and y == rows - 1:
        return result
    cost_by_candidate_moves = {}
    # if x > 0:
    #     cost_by_candidate_moves[(x-1, y)] = solve(x-1, y, rows, cols)
    if x < cols - 1:
        cost_by_candidate_moves[(x + 1, y)] = solve(x + 1, y, rows, cols, costs)
    if y < rows - 1:
        cost_by_candidate_moves[(x, y + 1)] = solve(x, y + 1, rows, cols, costs)
    result += min(cost_by_candidate_moves.values())

    memo[(x, y)] = result
    return result


def process(lines):
    rows = len(lines)
    if len(lines[-1]) == 0:
        rows -= 1
    cols = len(lines[0])

    return solve(0, 0, rows, cols, lines) - int(lines[0][0])


with open("/Users/viniciusgusmao/Documents/AoC2021/15.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    print process(lines)
