def low_points():

    result = 0

    with open("/Users/viniciusgusmao/Documents/AoC2021/9.txt") as file:
        matrix = []
        lines = file.read().split('\n')
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
                result += number + 1

    return result


print low_points()

