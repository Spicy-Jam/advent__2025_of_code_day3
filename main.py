def main():
    print("Hello from aoc25-day3!")
    day3_part1()
    day3_part2()

def day3_part1():
    joltages = open("/home/javan/workspace/advent_of_code_2025/aoc25_day3/aoc25_day3_input").read().split()

    required_joltages = []
    for joltage in joltages:
        required_joltages.append(int(p1_find_joltage(joltage)))
    
    print("Part 1 answer: ", sum(required_joltages))


def p1_find_joltage(joltage):
    max_joltage1 = -1
    max_joltage1_index = -1
    
    for digit in range(0, len(joltage)):
        joltage_to_check = int(joltage[digit])
        if joltage_to_check > max_joltage1:
            max_joltage1 = joltage_to_check
            max_joltage1_index = digit
    
    max_joltage2 = -1
    for digit in range(max_joltage1_index + 1, len(joltage)):
        joltage_to_check = int(joltage[digit])
        if joltage_to_check > max_joltage2:
            max_joltage2 = joltage_to_check

        
    required_joltage = (max_joltage1 * 10) + max_joltage2

    return required_joltage


def day3_part2():
    joltages = open("/home/javan/workspace/advent_of_code_2025/aoc25_day3/aoc25_day3_input").read().split()

    required_joltages = []
    for joltage in joltages:
        required_joltages.append(int(p2_find_joltage(joltage)))
    
    print("Part 2 answer: ", sum(required_joltages))
    

def p2_find_joltage(joltage):
    required_joltage = ""

    
    previous_max_index = -1
    for i in range(12):
        previous_max = 0
        for digit in range(previous_max_index + 1, len(joltage)):
            joltage_to_check = int(joltage[digit])
            if joltage_to_check > previous_max:
                previous_max = joltage_to_check
                previous_max_index = digit
        required_joltage += str(previous_max)

    return required_joltage


if __name__ == "__main__":
    main()
