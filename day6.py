import copy

# which position is forward?
orientations = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def rotate_right(orientation: str) -> str:
    return {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }[orientation]


def find_me(grid: list[list[str]]) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return (i, j)


def part2(
    grid: list[list[str]], path: set[tuple[int, int]], cur_x: int, cur_y: int
) -> int:
    count = 0
    for x, y in path:
        if grid[x][y] == "^" or grid[x][y] == "#":
            continue
        alt = copy.deepcopy(grid)
        alt[x][y] = "#"
        if len(part1(alt, cur_x, cur_y)) == 0:
            count += 1
    return count


def part1(grid: list[list[str]], cur_x: int, cur_y: int) -> set[tuple[int, int]]:
    me = "^"
    visited = set()
    visited_for_real_this_time = {}
    while cur_x < len(grid) and cur_y < len(grid[cur_x]):
        (x_off, y_off) = orientations[me]
        (next_x, next_y) = (cur_x + x_off), (cur_y + y_off)
        if (
            next_x < 0
            or next_x >= len(grid)
            or next_y < 0
            or next_y >= len(grid[next_x])
        ):
            break
        if grid[next_x][next_y] == "#":
            me = rotate_right(me)
            continue

        visited.add((next_x, next_y))
        visited_for_real_this_time[(next_x, next_y, me)] = (
            visited_for_real_this_time.get((next_x, next_y, me), 0) + 1
        )
        if visited_for_real_this_time[(next_x, next_y, me)] == 2:
            return []
        cur_x, cur_y = next_x, next_y

    return visited


if __name__ == "__main__":
    with open("input/day6.txt") as f:
        grid = [list(x.rstrip()) for x in f]
    (cur_x, cur_y) = find_me(grid)
    path = part1(grid, cur_x, cur_y)
    print(len(path))
    print(part2(grid, path, cur_x, cur_y))
