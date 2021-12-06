DAYS_TO_REPRO = 7
EXTRA_DAYS_AFTER_BIRTH = 2
SIMULATION_DAYS = 256


def process(counts):

    number_to_repro = counts[0]

    for i in range(DAYS_TO_REPRO + EXTRA_DAYS_AFTER_BIRTH - 1):
        counts[i] = counts[i + 1]

    counts[DAYS_TO_REPRO - 1] += number_to_repro
    counts[DAYS_TO_REPRO + EXTRA_DAYS_AFTER_BIRTH - 1] = number_to_repro


def lanternfish():
    
    with open("/Users/viniciusgusmao/Documents/AoC2021/6.txt") as file:
        numbers = file.read().split(',')

        counts = [0] * (DAYS_TO_REPRO + EXTRA_DAYS_AFTER_BIRTH)

        for number in numbers:
            counts[int(number)] += 1

        for i in range(SIMULATION_DAYS):
            process(counts)

        return sum(counts)


print lanternfish()

