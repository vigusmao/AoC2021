def fold(direction, axis, points):
    for i in range(len(points)):
        point = points[i]
        if point is None:
            continue
        x, y = point[0], point[1]
        if direction == 'x' and x > axis:
            points[i] = (2 * axis - x, y) if x <= 2 * axis else None
        elif direction == 'y' and y > axis:
            points[i] = (x, 2 * axis - y) if y <= 2 * axis else None


def plot_matrix(matrix):
    for row in matrix:
        print ''.join(row)


def draw(points, max_x, max_y):
    matrix = [[' '] * (max_y + 1) for x in range(max_x + 1)]
    for point in points:
        matrix[point[0]][point[1]] = "o"

    plot_matrix(matrix)


def process(lines):
    points = []

    for line in lines:
        if len(line) == 0:
            continue

        if line[0] == 'f':
            tokens = line.split('=')
            direction, axis = tokens[0][-1], int(tokens[1])
            fold(direction, axis, points)

        else:
            tokens = line.split(',')
            x, y = int(tokens[0]), int(tokens[1])
            points.append((x, y))

    points_set = set()
    max_x, max_y = 0, 0
    for point in points:
        if point is not None:
            points_set.add(point)
            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]

    draw(points_set, max_x, max_y)


with open("/Users/viniciusgusmao/Documents/AoC2021/13.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    process(lines)
