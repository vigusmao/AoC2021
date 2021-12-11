def flash(dumbo, flash_queue, flashed, levels):
    flashed.add(dumbo)
    row = dumbo[0]
    col = dumbo[1]
    if row > 0:
        if col > 0:
            increment_level((row - 1, col - 1), flash_queue, flashed, levels)
        increment_level((row - 1, col), flash_queue, flashed, levels)
        if col < 9:
            increment_level((row - 1, col + 1), flash_queue, flashed, levels)

    if col > 0:
        increment_level((row, col - 1), flash_queue, flashed, levels)
    increment_level((row, col), flash_queue, flashed, levels)
    if col < 9:
        increment_level((row, col + 1), flash_queue, flashed, levels)

    if row < 9:
        if col > 0:
            increment_level((row + 1, col - 1), flash_queue, flashed, levels)
        increment_level((row + 1, col), flash_queue, flashed, levels)
        if col < 9:
            increment_level((row + 1, col + 1), flash_queue, flashed, levels)


def increment_level(dumbo, flash_queue, flashed, levels):
    if dumbo in flashed:
        return
    row = dumbo[0]
    col = dumbo[1]
    levels[row][col] += 1
    if levels[row][col] == 10:
        flash_queue.append(dumbo)


def step(levels):
    flash_queue = []
    flashed = set()

    for row in range(10):
        for col in range(10):
            increment_level((row, col), flash_queue, flashed, levels)

    count_flashes = 0
    while len(flash_queue) > count_flashes:
        flash(flash_queue[count_flashes], flash_queue, flashed, levels)
        count_flashes += 1

    for dumbo in flashed:
        levels[dumbo[0]][dumbo[1]] = 0

    return len(flashed) == 100


def process(lines):
    levels = []
    for line in lines:
        levels.append([int(x) for x in line])

    step_idx = 1
    while True:
        if step(levels):
            return step_idx
        step_idx += 1


with open("/Users/viniciusgusmao/Documents/AoC2021/11.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    print process(lines)
