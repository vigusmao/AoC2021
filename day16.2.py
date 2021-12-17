def hex_digit_to_four_bits(x):
    binary = bin(int('0x' + x, 16))[2:]
    return '0' * (4 - len(binary)) + binary


def binary_to_decimal(x):
    return int('0b' + x, 2)


def compute(binary):
    pos = 0
    value = 0
    expression = None

    # skips version
    pos += 3

    packet_type = binary[pos : pos + 3]
    pos += 3

    if packet_type == '100':
        # literal
        while True:
            value *= 16
            value += binary_to_decimal(binary[pos + 1: pos + 5])
            expression = str(value)
            control = binary[pos]
            pos += 5
            if control == '0':
                break

    else:
        # operator and subpackets
        operands = []
        subexpressions = []

        length_type = binary[pos]
        pos += 1

        if length_type == '0':
            size_in_bits = binary_to_decimal(binary[pos: pos + 15])
            pos += 15
            max_pos = pos + size_in_bits
            while pos < max_pos:
                value, bits_read, subexpression = compute(binary[pos:])
                operands.append(value)
                subexpressions.append(subexpression)
                pos += bits_read

        else:
            number_of_subpackets = binary_to_decimal(binary[pos: pos + 11])
            pos += 11
            for i in range(number_of_subpackets):
                value, bits_read, subexpression = compute(binary[pos:])
                operands.append(value)
                subexpressions.append(subexpression)
                pos += bits_read

        if packet_type == '000':
            value = sum(operands)
            expression = '(' + '+'.join(subexpressions) + ')'
        elif packet_type == '001':
            if len(operands) > 0:
                value = 1
                for operand in operands:
                    value *= operand
                expression = '(' + '*'.join(subexpressions) + ')'
        elif packet_type == '010':
            value = min(operands)
            expression = 'min(' + ','.join(subexpressions) + ')'
        elif packet_type == '011':
            value = max(operands)
            expression = 'max(' + ','.join(subexpressions) + ')'
        elif packet_type == '101':
            value = 1 if operands[0] > operands[1] else 0
            expression = 'is_greater(' + ','.join(subexpressions) + ')'
        elif packet_type == '110':
            value = 1 if operands[0] < operands[1] else 0
            expression = 'is_less(' + ','.join(subexpressions) + ')'
        elif packet_type == '111':
            value = 1 if operands[0] == operands[1] else 0
            expression = 'are_equal(' + ','.join(subexpressions) + ')'

    return value, pos, expression


def process(line):
    binary_list = []
    for hex in line:
        if hex == '\n':
            continue
        binary_list.append(hex_digit_to_four_bits(hex))
    binary = ''.join(binary_list)

    return compute(binary)


with open("/Users/viniciusgusmao/Documents/AoC2021/16.txt") as file:
    line = file.read()
    print len(line) * 4
    value, bits_read, expression = process(line)
    print "%s = %d (%d bits read)" % (expression, value, bits_read)
