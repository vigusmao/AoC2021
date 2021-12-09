WIRES = 'abcdefg'

DIGIT_BY_SEGMENTS = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

SEGMENTS_BY_DIGIT_SIZE = []
for i in range(8):
    SEGMENTS_BY_DIGIT_SIZE.append(set())

for digit_segments in DIGIT_BY_SEGMENTS.keys():
    for segment in digit_segments:
        SEGMENTS_BY_DIGIT_SIZE[len(digit_segments)].add(segment)


def obtain_candidate_matchings(wires_list, candidate_segments_by_wire_map):
    for wires in wires_list.split():
        length = len(wires)
        for wire in wires:
            candidates_set = candidate_segments_by_wire_map.get(wire)
            if candidates_set is None:
                candidates_set = set()
                candidate_segments_by_wire_map[wire] = candidates_set

            candidates = SEGMENTS_BY_DIGIT_SIZE[length]
            if len(candidates_set) == 0:
                candidates_set |= candidates
            else:
                candidates_set &= candidates


def obtain_valid_matchings(matchings, current_matching, candidate_segments_by_wire, pos):
    if current_matching is None:
        current_matching = {}

    if pos == 7:
        return True

    next_wire = WIRES[pos]

    candidate_segments = candidate_segments_by_wire.get(next_wire)
    if candidate_segments is None:
        return False

    for candidate_segment in candidate_segments:
        if candidate_segment in current_matching.values():
            continue

        current_matching[next_wire] = candidate_segment

        if obtain_valid_matchings(matchings, current_matching, candidate_segments_by_wire, pos + 1):
            matchings.append(current_matching.copy())

        current_matching[next_wire] = None

    return False


def decode(wires_list, segment_by_wire):
    result = 0
    for wires in wires_list.split():
        result *= 10
        segments = []
        for wire in wires:
            segments.append(segment_by_wire[wire])
        segments.sort()
        digit = DIGIT_BY_SEGMENTS.get(''.join(segments))
        if digit is None:
            return None
        result += digit
    return result


def segments():

    result = 0

    with open("/Users/viniciusgusmao/Documents/AoC2021/8.txt") as file:
        lines = file.read().split('\n')
        for line in lines:
            subline = line.split('|')
            if len(subline) < 2:
                break

            ten_digits = subline[0]
            four_digits = subline[1]

            candidate_segments_by_wire = {}

            obtain_candidate_matchings(ten_digits, candidate_segments_by_wire)

            matchings = []
            obtain_valid_matchings(matchings, None, candidate_segments_by_wire, 0)

            for matching in matchings:
                number = decode(four_digits, matching)
                if number is not None:
                    result += number
                    break

    return result


print segments()

