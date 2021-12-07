POS_IDX = 0
COUNT_IDX = 1

def crabs(positions):
    
    count_by_pos = {}
    for pos in positions:
        count_by_pos[pos] = count_by_pos.get(pos, 0) + 1

    max_pos = max(positions)

    triangular_numbers = [0]
    for i in range(1, max_pos+1):
        triangular_numbers.append(triangular_numbers[i-1] + i)

    penalties = []
    for dest in range(max_pos + 1):
        penalties.append(sum((count * triangular_numbers[abs(origin - dest)] for origin, count in count_by_pos.items())))

    return min(penalties), penalties


with open("/Users/viniciusgusmao/Documents/AoC2021/7.txt") as file:
    positions = [int(x) for x in file.read().split(',')]

    print crabs(positions)

