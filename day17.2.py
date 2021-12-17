from math import ceil, sqrt

L = 236
R = 262

T = -58
B = -78


def within_target(x, y):
    return L <= x <= R and B <= y <= T


def reaches_target(vx, vy):
    min_steps = int(ceil((2 * vx + 1 - sqrt(4 * vx * vx + 4 * vx + 1 - 8 * L)) / 2))
    max_steps = vx
    s = min_steps
    pos_x = s * vx - (s * (s - 1)) / 2
    pos_y = s * vy - (s * (s - 1)) / 2

    while s < max_steps:
        if within_target(pos_x, pos_y):
            return True
        pos_x += vx - s
        pos_y += vy - s
        s += 1

    # at this point x is already not increasing
    while pos_y >= B:
        if within_target(pos_x, pos_y):
            return True
        pos_y += vy - s
        s += 1

    return False


def calculate_height(vx):
    steps_to_reach_L = int(ceil((2 * vx + 1 - sqrt(4 * vx * vx + 4 * vx + 1 - 8 * L)) / 2))

    vy_min = int(ceil((2 * B + steps_to_reach_L * (steps_to_reach_L - 1)) / (2 * steps_to_reach_L)))
    vy_max = 1 - B

    count = 0

    for vy in range(vy_min, vy_max + 1):
        if reaches_target(vx, vy):
            count += 1

    return count


vx_min = int(ceil((sqrt(8*L + 1) - 1) / 2))
vx_max = R

count_overall = 0

max_height = 0
for vx in range(vx_min, vx_max + 1):
    count_overall += calculate_height(vx)

print count_overall



