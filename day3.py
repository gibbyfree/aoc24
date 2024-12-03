import re


def part1(line: str) -> int:
    sum = 0
    matches = re.findall("mul\(\d+,\d+\)", line)
    for match in matches:
        split = match.split(",")
        a = int(split[0][4:])
        b = int(split[1][:-1])
        sum += a * b
    return sum


def part2(line: str) -> int:
    sum = 0
    matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            split = match.split(",")
            a = int(split[0][4:])
            b = int(split[1][:-1])
            sum += a * b
    return sum


if __name__ == "__main__":
    with open("input/day3.txt") as f:
        linestr = f.read().strip()
    print(part1(linestr))
    print(part2(linestr))
