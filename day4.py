def part1(grid: list[list[str]]) -> int:
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                # check for word in all possible directions
                # left and right
                if j + 4 <= len(grid[i]):
                    if [grid[i][j + k] for k in range(4)] == list("XMAS"):
                        sum += 1
                if j >= 3:
                    if [grid[i][j - k] for k in range(4)] == list("XMAS"):
                        sum += 1
                # up and down
                if i + 4 <= len(grid):
                    if [grid[i + k][j] for k in range(4)] == list("XMAS"):
                        sum += 1
                if i >= 3:
                    if [grid[i - k][j] for k in range(4)] == list("XMAS"):
                        sum += 1
                # diagonals
                if i + 4 <= len(grid) and j + 4 <= len(grid[i]):
                    if [grid[i + k][j + k] for k in range(4)] == list("XMAS"):
                        sum += 1
                if i + 4 <= len(grid) and j >= 3:
                    if [grid[i + k][j - k] for k in range(4)] == list("XMAS"):
                        sum += 1
                if i >= 3 and j + 4 <= len(grid[i]):
                    if [grid[i - k][j + k] for k in range(4)] == list("XMAS"):
                        sum += 1
                if i >= 3 and j >= 3:
                    if [grid[i - k][j - k] for k in range(4)] == list("XMAS"):
                        sum += 1
    return sum


def part2(grid: list[list[str]]) -> int:
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (
                grid[i][j] == "A"
                and j >= 1
                and i >= 1
                and i < len(grid) - 1
                and j < len(grid[i]) - 1
            ):
                a, b, c, d = (
                    grid[i - 1][j - 1],  # top left
                    grid[i + 1][j + 1],  # bottom right
                    grid[i - 1][j + 1],  # top right
                    grid[i + 1][j - 1],  # bottom left
                )
                if ([a, b] == ["M", "S"] or [a, b] == ["S", "M"]) and (
                    [c, d] == ["M", "S"] or [c, d] == ["S", "M"]
                ):
                    sum += 1
    return sum


if __name__ == "__main__":
    with open("input/day4.txt") as f:
        grid = [list(x.rstrip()) for x in f]
    print(part1(grid))
    print(part2(grid))
