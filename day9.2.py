def populate_basin(root, basin, matrix):
    row = root[0]
    col = root[1]
    number = matrix[row][col]
    if number == 9:
        return

    basin.add(root)
    matrix[row][col] = 9

    rows = len(matrix)
    cols = len(matrix[0])

    # left
    if col > 0 and number < matrix[row][col - 1]:
        populate_basin((row, col - 1), basin, matrix)
    # right
    if col < cols - 1 and number < matrix[row][col + 1]:
        populate_basin((row, col + 1), basin, matrix)
    # up
    if row > 0 and number < matrix[row - 1][col]:
        populate_basin((row - 1, col), basin, matrix)
    # down
    if row < rows - 1 and number < matrix[row + 1][col]:
        populate_basin((row + 1, col), basin, matrix)


def find_basins(matrix, low_points):
    result = []

    for low_point in low_points:
        basin = set()
        populate_basin(low_point, basin, matrix)
        result.append((len(basin), basin))

    return result


def find_low_points(lines):

    result = []

    for line in lines:
        if len(line) > 0:
            matrix.append([int(x) for x in line])

    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            number = matrix[row][col]
            # left
            if col > 0 and number >= matrix[row][col - 1]:
                continue
            # right
            if col < cols - 1 and number >= matrix[row][col + 1]:
                continue
            # up
            if row > 0 and number >= matrix[row - 1][col]:
                continue
            # down
            if row < rows - 1 and number >= matrix[row + 1][col]:
                continue
            result.append((row, col))

    return result


with open("/Users/viniciusgusmao/Documents/AoC2021/9.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    low_points = find_low_points(lines)
    basins = find_basins(matrix, low_points)
    basins.sort()
    print basins[-1][0] * basins[-2][0] * basins[-3][0]
