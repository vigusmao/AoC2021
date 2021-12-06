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


def vertical_overlap(line1, line2):
    if line1[ORIG][X] != line2[ORIG][X]:
        return None
    if line1[ORIG][Y] <= line2[ORIG][Y] <= line1[DEST][Y]:
        return [(line1[ORIG][X], y) for y in xrange(line2[ORIG][Y], min(line1[DEST][Y], line2[DEST][Y]) + 1)]
    if line2[ORIG][Y] <= line1[ORIG][Y] <= line2[DEST][Y]:
        return [(line2[ORIG][X], y) for y in xrange(line1[ORIG][Y], min(line2[DEST][Y], line1[DEST][Y]) + 1)]


def horizontal_overlap(line1, line2):
    if line1[ORIG][Y] != line2[ORIG][Y]:
        return None
    if line1[ORIG][X] <= line2[ORIG][X] <= line1[DEST][X]:
        return [(x, line1[ORIG][Y]) for x in xrange(line2[ORIG][X], min(line1[DEST][X], line2[DEST][X]) + 1)]
    if line2[ORIG][X] <= line1[ORIG][X] <= line2[DEST][X]:
        return [(x, line2[ORIG][Y]) for x in xrange(line1[ORIG][X], min(line2[DEST][X], line1[DEST][X]) + 1)]


def orthogonal_overlap(vertical_line, horizontal_line):
    if horizontal_line[ORIG][X] <= vertical_line[ORIG][X] <= horizontal_line[DEST][X] and \
            vertical_line[ORIG][Y] <= horizontal_line[ORIG][Y] <= vertical_line[DEST][Y]:
        return vertical_line[ORIG][X], horizontal_line[ORIG][Y]
    return None


def add_intersection_point(point, intersections):
    intersections.add(point)


def wind():

    with open("/Users/viniciusgusmao/Documents/AoC2021/5.txt") as file:
        content = file.read().split('\n')

        vertical_lines = []
        horizontal_lines = []
        oblique_lines = []

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

        for i in range(len(vertical_lines)):
            line1 = vertical_lines[i]
            for j in range(i + 1, len(vertical_lines)):
                line2 = vertical_lines[j]
                overlap = vertical_overlap(line1, line2)
                if overlap is not None:
                    for point in overlap:
                        add_intersection_point(point, intersections)

        for i in range(len(horizontal_lines)):
            line1 = horizontal_lines[i]
            for j in range(i + 1, len(horizontal_lines)):
                line2 = horizontal_lines[j]
                overlap = horizontal_overlap(line1, line2)
                if overlap is not None:
                    for point in overlap:
                        add_intersection_point(point, intersections)

        for i in range(len(vertical_lines)):
            line1 = vertical_lines[i]
            for j in range(len(horizontal_lines)):
                line2 = horizontal_lines[j]
                point = orthogonal_overlap(line1, line2)
                if point is not None:
                    add_intersection_point(point, intersections)

        return len(intersections)


start = time()
print wind()
print "elapsed time = %.6f seconds" % (time() - start)



