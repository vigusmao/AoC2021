

def process(lines):
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        if len(line) == 0:
            continue
        rule = line.split(' -> ')
        rules[rule[0]] = rule[1]

    for i in range(10):
        new_template = [template[0]]
        for i in range(len(template) - 1):
            pair = template[i] + template[i+1]
            middle = rules.get(pair)
            if middle is not None:
                new_template.append(middle)
            new_template.append(pair[1])
        template = ''.join(new_template)

    counts = {}
    for c in template:
        new_count = counts.get(c, 0) + 1
        counts[c] = new_count

    return max(counts.values()) - min(counts.values())


with open("/Users/viniciusgusmao/Documents/AoC2021/14.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    print process(lines)
