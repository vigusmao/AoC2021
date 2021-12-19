from math import floor, ceil


def is_number(char):
    return '0' <= char <= '9'


def reduce(fish):

    done = False

    while not done:

        # explosions

        exploded_any = False
        open_positions = []

        for i in xrange(len(fish)):
            c = fish[i]
            if c == '[':
                open_positions.append(i)
            elif c == ']':
                open_pos = open_positions.pop();
                if len(open_positions) == 4:
                    # has completely parsed a snailfish that must explode

                    # adds to the left
                    numbers_to_explode = (eval(fish[open_pos + 1]), eval(fish[open_pos + 3]))
                    for j in xrange(open_pos - 2, 0, -1):
                        if is_number(fish[j]):
                            new_number = numbers_to_explode[0] + eval(fish[j])
                            fish[j] = str(new_number)
                            break

                    # adds to the right
                    for j in xrange(i + 2, len(fish)):
                        if is_number(fish[j]):
                            new_number = numbers_to_explode[1] + eval(fish[j])
                            fish[j] = str(new_number)
                            break

                    fish[open_pos: open_pos + 5] = ['0']

                    exploded_any = True
                    break

            i += 1

        if exploded_any:
            continue

        # splits

        split_any = False

        for i in xrange(len(fish) - 1):
            c = fish[i]
            if is_number(c):
                number = eval(fish[i])
                if number >= 10:
                    fish[i: i+1] = ['[', str(int(floor(number / 2))), ',', str(int(ceil(number / 2.0))), ']']
                    split_any = True
                    break

        if not split_any:
            break


def add_snailfishes(fish0, fish1):
    return ['['] + fish0 + [','] + fish1 + [']']


def get_magnitude(snailfish):
    if is_number(str(snailfish)):
        return snailfish

    return 3 * get_magnitude(snailfish[0]) + 2 * get_magnitude(snailfish[1])


def process(lines):
    best = 0
    for i in xrange(0, len(lines)):
        if len(lines[i]) == 0:
            continue
        snailfish1 = list(lines[i])
        for j in xrange(0, len(lines)):
            if len(lines[j]) == 0:
                continue
            if j == i:
                continue
            snailfish2 = list(lines[j])
            result = add_snailfishes(snailfish1, snailfish2)
            reduce(result)
            best = max(best, get_magnitude(eval(''.join(result))))

    return best


with open("/Users/viniciusgusmao/Documents/AoC2021/18.txt") as file:
    lines = file.read().split('\n')
    print process(lines)
