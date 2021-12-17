EXPRESSION_BY_OPERATOR = {
    '000': ('(', ' + ', ')'),
    '001': ('(', ' * ', ')'),
    '010': ('min([', ', ', '])'),
    '011': ('max([', ', ', '])'),
    '100': ('', '', ''),
    '101': ('(', ' > ', ')'),
    '110': ('(', ' < ', ')'),
    '111': ('(', ' == ', ')')
}


def obtain_expression(operator, operands):
    prefix, joiner, suffix = EXPRESSION_BY_OPERATOR.get(operator)
    return prefix + joiner.join(operands) + suffix


def hexa_symbol_to_four_bits(x):
    binary = bin(int('0x' + x, 16))[2:]
    return '0' * (4 - len(binary)) + binary


def binary_to_decimal(x):
    return int('0b' + x, 2)


def compute(binary):
    pos = 0
    value = 0
    operands = []

    # skips version
    pos += 3

    packet_type = binary[pos : pos + 3]
    pos += 3

    if packet_type == '100':
        # literal

        while True:
            value *= 16
            value += binary_to_decimal(binary[pos + 1: pos + 5])
            control = binary[pos]
            pos += 5
            if control == '0':
                break
        operands.append(str(value))

    else:
        # operator and subpackets

        length_type = binary[pos]
        pos += 1

        if length_type == '0':
            size_in_bits = binary_to_decimal(binary[pos: pos + 15])
            pos += 15
            max_pos = pos + size_in_bits
            while pos < max_pos:
                subexpression, bits_read = compute(binary[pos:])
                operands.append(subexpression)
                pos += bits_read

        else:
            number_of_subpackets = binary_to_decimal(binary[pos: pos + 11])
            pos += 11
            for i in range(number_of_subpackets):
                subexpression, bits_read = compute(binary[pos:])
                operands.append(subexpression)
                pos += bits_read

    return obtain_expression(packet_type, operands), pos


def process(hexa):
    binary_as_list = []
    for h in hexa:
        if h == '\n':
            continue
        binary_as_list.append(hexa_symbol_to_four_bits(h))
    binary = ''.join(binary_as_list)

    return compute(binary)


with open("/Users/viniciusgusmao/Documents/AoC2021/16.txt") as file:
    line = file.read()
    expression, size = process(line)
    print "%s = %d (%d bits read)" % (expression, eval(expression), size)
