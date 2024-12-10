import itertools


def compute_result(result: str) -> int:
    current_operator = ""
    result_list = result.split()

    val = int(result_list[0])
    num = -1

    for token in result_list[1:]:
        if token.isdigit():
            num = int(token)
        elif token == "+" or token == "*" or token == "||":
            current_operator = token

        if current_operator == "+" and num != -1:
            val += num
            num = -1
        elif current_operator == "*" and num != -1:
            val *= num
            num = -1
        elif current_operator == "||" and num != -1:
            val = int(str(val) + str(num))
            num = -1

    return val


def part1(lines: list[str], operators: list[str]) -> int:
    count = 0
    for line in lines:
        target, vals = line.split(": ")
        target = int(target)
        vals = list(map(int, vals.split()))
        operator_slots = len(vals) - 1

        # produce an eval string for all possible combinations
        # ... but eval respects PEMDAS so compute manually
        result = ""
        for combination in itertools.product(operators, repeat=operator_slots):
            result = str(vals[0])
            for i, operator in enumerate(combination):
                result += f" {operator} {vals[i + 1]}"
            if compute_result(result) == target:
                count += target
                break
    return count


if __name__ == "__main__":
    with open("input/day7.txt") as f:
        lines = list(f)
    print(part1(lines, ["+", "*"]))
    print(part1(lines, ["+", "*", "||"]))
