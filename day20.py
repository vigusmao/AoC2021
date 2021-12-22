def obtain_image_bit(row, col, image, non_existing_pixel_bit):
    rows = len(image)
    cols = len(image[0])
    if col < 0 or col >= cols or row < 0 or row >= rows:
        return non_existing_pixel_bit
    return 1 if image[row][col] == '#' else 0


def compute_enhanced_pixel(row, col, image, pattern, non_existing_pixel_bit):
    binary_as_list = []
    for r in xrange(row - 1, row + 2):
        for c in xrange(col - 1, col + 2):
            binary_as_list.append(str(obtain_image_bit(r, c, image, non_existing_pixel_bit)))
    pattern_bit_idx = int(''.join(binary_as_list), 2)
    return pattern[pattern_bit_idx]


def enhance(image, pattern, enhancement_idx):
    non_existing_pixel_bit = 1 - enhancement_idx % 2 if pattern[0] == '#' and pattern[511] == '.' else 0
    enhanced_image = []
    for row in range(-1, len(image) + 1):
        enhanced_row = []
        for col in range(-1, len(image[0]) + 1):
            enhanced_row.append(compute_enhanced_pixel(row, col, image, pattern, non_existing_pixel_bit))
        enhanced_image.append(enhanced_row)
    return enhanced_image


def print_image(image):
    for row in image:
        print ''.join(row)
    print len(image), len(image[0]), len(image[-1])


def process(lines):
    pattern = lines[0]
    print pattern[511]
    image = lines[2:]
    if len(image[-1]) == 0:
        image[-1:] = []

    for i in xrange(1, 51):
        image = enhance(image, pattern, i)

    return sum(sum(1 if c == '#' else 0 for c in row) for row in image)


with open("/Users/viniciusgusmao/Documents/AoC2021/20.txt") as file:
    lines = file.read().split('\n')
    print process(lines)
