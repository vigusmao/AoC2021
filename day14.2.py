

def process(lines):
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        if len(line) == 0:
            continue
        rule = line.split(' -> ')
        rules[rule[0]] = rule[1]

    count_by_active_pair = {}
    count_by_inactive_pair = {}

    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        if pair in rules:
            count_by_active_pair[pair] = count_by_active_pair.get(pair, 0) + 1
        else:
            count_by_inactive_pair[pair] = count_by_inactive_pair.get(pair, 0) + 1

    for _ in range(40):
        new_count_by_active_pair = {}

        for pair, count in count_by_active_pair.items():
            middle = rules.get(pair)
            new_pair_1 = pair[0] + middle
            new_pair_2 = middle + pair[1]
            if new_pair_1 in rules:
                new_count_by_active_pair[new_pair_1] = new_count_by_active_pair.get(new_pair_1, 0) + count
            else:
                count_by_inactive_pair[new_pair_1] = count_by_inactive_pair.get(new_pair_1, 0) + count
            if new_pair_2 in rules:
                new_count_by_active_pair[new_pair_2] = new_count_by_active_pair.get(new_pair_2, 0) + count
            else:
                count_by_inactive_pair[new_pair_2] = count_by_inactive_pair.get(new_pair_2, 0) + count
            count_by_active_pair = new_count_by_active_pair

    counts_by_char = {}
    for pair, count in count_by_active_pair.items():
        counts_by_char[pair[1]] = counts_by_char.get(pair[1], 0) + count
    for pair, count in count_by_inactive_pair.items():
        counts_by_char[pair[1]] = counts_by_char.get(pair[1], 0) + count
    counts_by_char[template[0]] += 1

    return max(counts_by_char.values()) - min(counts_by_char.values())


with open("/Users/viniciusgusmao/Documents/AoC2021/14.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    print process(lines)
