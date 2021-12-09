def count_easy_digits(digits):
    result = 0
    for segments in digits.split():
        if len(segments) in [2, 3, 4, 7]:
            result += 1
    return result


def segments():

    result = 0

    with open("/Users/viniciusgusmao/Documents/AoC2021/8.txt") as file:
        lines = file.read().split('\n')
        for line in lines:
            subline = line.split('|')
            if len(subline) < 2:
                break
            four_digits = subline[1]
            result += count_easy_digits(four_digits)

    return result


print segments()

