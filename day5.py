from collections import defaultdict


def reorder(
    seconds: defaultdict[list],
    line: list[int],
    remaining: set[int],
    bad: int,
) -> int:
    # Swap order of bad with a second
    valid = seconds[line[bad]]
    for candidate in valid:
        if candidate in remaining:
            candidate_idx = line.index(candidate)
            line[candidate_idx] = line[bad]
            line[bad] = candidate
            return validate(seconds, line, reordered=True)
    return 0


def validate(
    seconds: defaultdict[list],
    line: list[int],
    reordered: bool = False,
) -> int:
    read = []
    remaining = set(line)
    copy = line[:]
    for i, val in enumerate(line):
        if not read and (
            not seconds[val] or all(r not in seconds[val] for r in remaining)
        ):
            read.append(val)  # first entry
            remaining.remove(val)
        elif not any(r in seconds[val] for r in remaining):
            read.append(val)
            remaining.remove(val)
        else:
            return reorder(seconds, copy, remaining, i)
    return copy[len(line) // 2] if reordered else 0


def both(seconds: defaultdict[list], commands: list[list[int]]):
    middles = []
    reordered_middles = []
    for line in commands:
        result = validate(seconds, line[:])
        if result == 0:
            middles.append(line[len(line) // 2])
        else:
            reordered_middles.append(result)
    return (sum(middles), sum(reordered_middles))


if __name__ == "__main__":
    with open("input/day5.txt") as f:
        lines = list(f)

        seconds = defaultdict(list)
        commands = []
        command_time = False

        for line in lines:
            if line == "\n":
                command_time = True
                continue

            if command_time:
                commands.append(list(map(int, line.split(","))))
            else:
                a, b = map(int, line.split("|"))
                seconds[b].append(a)

    print(both(seconds, commands))
