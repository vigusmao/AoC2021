# readability consts
X = 0
Y = 1
Z = 2
START = 0
END = 1
COMMAND = 0
RANGES = 1


def process(lines):
    switched_on_cubes = set()
    cuboids = []

    for line in lines:
        if len(line) == 0:
            continue
        tokens = line.split(' ')
        command = tokens[0] == 'on'
        ranges_token = tokens[1].split(',')
        ranges = [ranges_token[X][2:].split('..'),
                  ranges_token[Y][2:].split('..'),
                  ranges_token[Z][2:].split('..')]
        ranges[X] = (int(ranges[X][START]), int(ranges[X][END]))
        ranges[Y] = (int(ranges[Y][START]), int(ranges[Y][END]))
        ranges[Z] = (int(ranges[Z][START]), int(ranges[Z][END]))
        if ranges[X][START] < -50 or ranges[X][END] > 50 or \
                ranges[Y][START] < -50 or ranges[Y][END] > 50 or \
                ranges[Z][START] < -50 or ranges[Z][END] > 50:
            continue
        cuboids.append((command, ranges))

    for cuboid in cuboids:
        command = cuboid[COMMAND]
        ranges = cuboid[RANGES]
        for x in xrange(ranges[X][START], ranges[X][END] + 1):
            for y in xrange(ranges[Y][START], ranges[Y][END] + 1):
                for z in xrange(ranges[Z][START], ranges[Z][END] + 1):
                    cube = (x, y, z)

                    if command:
                        switched_on_cubes.add(cube)
                    elif cube in switched_on_cubes:
                        switched_on_cubes.remove(cube)

    return len(switched_on_cubes)


with open("/Users/viniciusgusmao/Documents/AoC2021/22test.txt") as file:
    lines = file.read().split('\n')
    print process(lines)
