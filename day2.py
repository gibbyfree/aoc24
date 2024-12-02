from time import perf_counter_ns


def valid_pair(first: int, second: int, inc: bool) -> bool:
    return (
        (first != second)
        and abs(first - second) <= 3
        and ((first > second and not inc) or (first < second and inc))
    )


def valid_line(line: list[int], dampen: bool = False) -> bool:
    inc = line[0] < line[1]
    removed = False
    i = 0
    while i < len(line) - 1:
        first, second = line[i], line[i + 1]
        if not valid_pair(first, second, inc):
            if dampen and not removed:
                i += 1
                removed = True
                continue
            else:
                return False
        i += 1
    return True


def part1(lines: list[list[int]]) -> int:
    return sum(1 for line in lines if valid_line(line))


def part2(lines: list[list[int]]) -> int:
    return sum(1 for line in lines if valid_line(line, True))


if __name__ == "__main__":
    start = perf_counter_ns()
    with open("input/day2.txt") as f:
        lines_str = [x.rstrip() for x in f]
        lines = [list(map(int, x.split())) for x in lines_str]

    print(part1(lines))
    print(part2(lines))
    print(f"Time: {perf_counter_ns() - start}ns")
