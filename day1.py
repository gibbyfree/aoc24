from collections import Counter
from time import perf_counter_ns


def part1(left: list[str], right: list[str]) -> int:
    lows, highs = sorted(left), sorted(right)
    return sum([abs(int(high) - int(low)) for low, high in zip(lows, highs)])


def part2(left: list[str], right: list[str]) -> int:
    right_counts = Counter(right)
    return sum([right_counts[x] * int(x) if x in right_counts else 0 for x in left])


if __name__ == "__main__":
    start = perf_counter_ns()
    with open("input/day1.txt") as f:
        lines = [x.rstrip() for x in f]
        left, right = map(list, zip(*(s.split() for s in lines)))

    print(part1(left, right))
    print(part2(left, right))
    print(f"Time: {perf_counter_ns() - start}ns")
