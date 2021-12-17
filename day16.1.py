def hex_digit_to_four_bits(x):
    binary = bin(int('0x' + x, 16))[2:]
    return '0' * (4 - len(binary)) + binary


def binary_to_decimal(x):
    return int('0b' + x, 2)


def obtain_versions_sum(binary, number_of_packets=1):
    result = 0
    pos = 0
    packets_count = 0

    while pos < len(binary):

        result += binary_to_decimal(binary[pos : pos + 3])
        pos += 3
        type = binary[pos : pos + 3]
        pos += 3

        if type == '100':
            # literal
            while True:
                block = binary[pos : pos + 5]
                pos += 5
                if len(block) == 0 or block[0] == '0':
                    break

        else:
            # operator and subpackets
            length_type = binary[pos]
            pos += 1
            if length_type == '0':
                size_in_bits = binary_to_decimal(binary[pos : pos + 15])
                pos += 15
                subpackets = binary[pos : pos + size_in_bits]
                versions, bits_read = obtain_versions_sum(subpackets, None)
                result += versions
                pos += bits_read

            else:
                number_of_subpackets = binary_to_decimal(binary[pos : pos + 11])
                pos += 11
                versions, bits_read = obtain_versions_sum(binary[pos:], number_of_subpackets)
                result += versions
                pos += bits_read

        packets_count += 1

        if number_of_packets is not None and packets_count == number_of_packets:
            break

    return result, pos


def process(line):
    binary_list = []
    for hex in line:
        if hex == '\n':
            continue
        binary_list.append(hex_digit_to_four_bits(hex))
    binary = ''.join(binary_list)

    print(line)
    print(binary)

    return obtain_versions_sum(binary)


with open("/Users/viniciusgusmao/Documents/AoC2021/16.txt") as file:
    line = file.read()
    print process(line)[0]
