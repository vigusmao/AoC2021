from math import sqrt
from itertools import permutations

X = 0
Y = 1
Z = 2


def dist_r3(point1, point2):
    return int(sqrt((point1[X] - point2[X]) ** 2 + (point1[Y] - point2[Y]) ** 2 + (point1[Z] - point2[Z]) ** 2))


def add_scanner_beacons(scanner, coordinates_by_triangle_by_scanner, offset_by_scanner, all_beacons):
    offset = offset_by_scanner[scanner]
    for vertices in coordinates_by_triangle_by_scanner.get(scanner).values():
        for vertex in vertices:
            translated_beacon = (vertex[X] + offset[X],
                                 vertex[Y] + offset[Y],
                                 vertex[Z] + offset[Z])
            all_beacons.add(translated_beacon)


def transform_beacons(beacons, permutation, orientation):
    return [transform_beacon(beacon, permutation, orientation) for beacon in beacons]


def transform_beacon(beacon, permutation, orientation):
    return tuple(beacon[permutation[i]] * orientation[i] for i in [0, 1, 2])


def process(lines):
    points_list_by_scanner = []
    points_list = None

    for line in lines:
        if len(line) == 0:
            continue
        if line.startswith('---'):
            points_list = []
            points_list_by_scanner.append(points_list)
        else:
            points_list.append(eval(line))

    coordinates_by_quadrilateral_by_scanner = {}

    for idx, points_list in enumerate(points_list_by_scanner):

        coordinates_by_quadrilateral = {}

        for i in xrange(len(points_list) - 3):
            point1 = points_list[i]
            for j in xrange(i + 1, len(points_list) - 2):
                point2 = points_list[j]
                for k in xrange(j + 1, len(points_list) - 1):
                    point3 = points_list[k]
                    for l in xrange(k + 1, len(points_list)):
                        point4 = points_list[l]

                        quadrilateral = [dist_r3(point1, point2), dist_r3(point1, point3), dist_r3(point1, point4),
                                         dist_r3(point2, point3), dist_r3(point2, point4), dist_r3(point3, point4)]
                        quadrilateral.sort()
                        coordinates_by_quadrilateral[tuple(quadrilateral)] = (point1, point2, point3, point4)

        coordinates_by_quadrilateral_by_scanner[idx] = coordinates_by_quadrilateral

    all_beacons = set()
    offset_by_scanner = {0: (0, 0, 0)}
    permutation_by_scanner = {0: (X, Y, Z)}
    orientation_by_scanner = {0: (1, 1, 1)}

    # first add all beacons as seen by scanner 0
    add_scanner_beacons(0, coordinates_by_quadrilateral_by_scanner, offset_by_scanner, all_beacons)
    origins = [0]

    while len(origins) > 0:
        r = origins.pop()  # reference scanner
        reference_offset = offset_by_scanner.get(r)

        for s in xrange(len(points_list_by_scanner)):
            if s == r or s in offset_by_scanner:
                continue

            common_quadrilaterals = set(coordinates_by_quadrilateral_by_scanner[r].keys()) & \
                                    set(coordinates_by_quadrilateral_by_scanner[s].keys())

            if len(common_quadrilaterals) >= 220:
                common_beacons = {r: set(), s: set()}
                for t in common_quadrilaterals:
                    common_beacons[r] |= {c for c in coordinates_by_quadrilateral_by_scanner[r].get(t)}
                    common_beacons[s] |= {c for c in coordinates_by_quadrilateral_by_scanner[s].get(t)}
                common_beacons[r] = list(common_beacons[r])
                common_beacons[s] = list(common_beacons[s])

                reference = common_beacons[r]
                reference.sort()

                for permutation in permutations([X, Y, Z]):
                    success = False

                    for x in xrange(8):
                        binary = bin(x)[2:]
                        binary = '0' * (3 - len(binary)) + binary
                        orientation = (1 if binary[0] == '1' else -1,
                                       1 if binary[1] == '1' else -1,
                                       1 if binary[2] == '1' else -1)

                        success = True
                        offset = None

                        transformed_beacons = transform_beacons(common_beacons[s], permutation, orientation)
                        transformed_beacons.sort()

                        for beacon_idx in xrange(len(common_beacons[s])):
                            reference_beacon = reference[beacon_idx]
                            transformed_beacon = transformed_beacons[beacon_idx]

                            if offset is None:
                                offset = (reference_beacon[X] - transformed_beacon[X],
                                          reference_beacon[Y] - transformed_beacon[Y],
                                          reference_beacon[Z] - transformed_beacon[Z])
                                continue

                            if reference_beacon[X] - transformed_beacon[X] != offset[X]:
                                success = False
                                break
                            if reference_beacon[Y] - transformed_beacon[Y] != offset[Y]:
                                success = False
                                break
                            if reference_beacon[Z] - transformed_beacon[Z] != offset[Z]:
                                success = False
                                break

                        if success:
                            offset_by_scanner[s] = (offset[X] + reference_offset[X],
                                                    offset[Y] + reference_offset[Y],
                                                    offset[Z] + reference_offset[Z])
                            permutation_by_scanner[s] = permutation
                            orientation_by_scanner[s] = orientation

                            for quadrilateral, quadrilateral_vertices in coordinates_by_quadrilateral_by_scanner[s].items():
                                coordinates_by_quadrilateral_by_scanner[s][quadrilateral] = tuple(transform_beacons(
                                    quadrilateral_vertices, permutation, orientation))

                            add_scanner_beacons(s, coordinates_by_quadrilateral_by_scanner, offset_by_scanner, all_beacons)
                            origins.append(s)
                            break  # for x...

                    if success:
                        break  # for permutation...

    return len(all_beacons)


with open("/Users/viniciusgusmao/Documents/AoC2021/19.txt") as file:
    lines = file.read().split('\n')
    print process(lines)
