from time import time

X = 0
Y = 1
ORIG = 0
DEST = 1


def is_vertical(line):
    return line[ORIG][X] == line[DEST][X]


def is_horizontal(line):
    return line[ORIG][Y] == line[DEST][Y]


def canonical_vertical(line):
    return (line[DEST], line[ORIG]) if line[ORIG][Y] > line[DEST][Y] else line


def canonical_horizontal(line):
    return (line[DEST], line[ORIG]) if line[ORIG][X] > line[DEST][X] else line


def add_point(point, count_by_point, intersections):
    new_count = count_by_point.get(point, 0) + 1
    count_by_point[point] = new_count
    if new_count == 2:
        intersections.add(point)


def add_all_line_points(line, count_by_point, intersections):
    if is_vertical(line):
        for y in range(line[ORIG][Y], line[DEST][Y] + 1):
            add_point((line[ORIG][X], y), count_by_point, intersections)

    elif is_horizontal(line):
        for x in range(line[ORIG][X], line[DEST][X] + 1):
            add_point((x, line[ORIG][Y]), count_by_point, intersections)

    else:
        offset_y =  1 if line[DEST][Y] > line[ORIG][Y] else -1
        point = line[ORIG]
        while point[X] <= line[DEST][X]:
            add_point(point, count_by_point, intersections)
            point = (point[X] + 1, point[Y] + offset_y)


def wind():

    with open("/Users/viniciusgusmao/Documents/AoC2021/5.txt") as file:
        content = file.read().split('\n')

        vertical_lines = []
        horizontal_lines = []
        oblique_lines = []

        count_by_point = {}
        intersections = set()

        for line in content:
            coords = line.split(' -> ')
            if len(coords) < 2:
                break
            coord1 = tuple(int(x) for x in coords[0].split(','))
            coord2 = tuple(int(x) for x in coords[1].split(','))

            line = (coord1, coord2)

            if is_vertical(line):
                vertical_lines.append(canonical_vertical(line))
            elif is_horizontal(line):
                horizontal_lines.append(canonical_horizontal(line))
            else:
                oblique_lines.append(canonical_horizontal(line))

        for line in vertical_lines:
            add_all_line_points(line, count_by_point, intersections)
        for line in horizontal_lines:
            add_all_line_points(line, count_by_point, intersections)

        # ----------------------------------------------------
        # Uncomment the two lines below to run PART TWO
        # for line in oblique_lines:
        #     add_points(line, count_by_point, intersections)
        # ----------------------------------------------------

        return len(intersections)


start = time()
print wind()
print "elapsed time = %.6f seconds" % (time() - start)



