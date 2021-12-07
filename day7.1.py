NUMBER_IDX = 0
COUNT_IDX = 1

def crabs(positions):
    
    counts = {}
    for pos in positions:
        counts[pos] = counts.get(pos, 0) + 1

    pos_with_counts = sorted([(pos,  count) for pos, count in counts.items()])

    suffix_count = []
    accrued = 0
    for i in range(len(pos_with_counts) - 1, -1, -1):
        accrued += pos_with_counts[i][COUNT_IDX]
        suffix_count.append(accrued)
    suffix_count.reverse()

    penalties = [sum(((pos_with_counts[i][NUMBER_IDX] - pos_with_counts[i-1][NUMBER_IDX]) * suffix_count[i]
                      for i in range(1, len(pos_with_counts))))]

    for i in range(1, len(pos_with_counts)):
        shift = pos_with_counts[i][NUMBER_IDX] - pos_with_counts[i - 1][NUMBER_IDX]
        increased_dist_crabs = suffix_count[0] - suffix_count[i]
        decreased_dist_crabs = suffix_count[i]
        penalty = penalties[i - 1] + shift * (increased_dist_crabs - decreased_dist_crabs)
        penalties.append(penalty)

    return min(penalties), penalties


with open("/Users/viniciusgusmao/Documents/AoC2021/7.txt") as file:
    numbers = [int(x) for x in file.read().split(',')]

    print crabs(numbers)

