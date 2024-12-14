from collections import defaultdict


def solve(antenna_coords: defaultdict[str, list]) -> tuple[int, int]:
    part1_antinode_coords = set()
    part2_antinode_coords = set()

    for key in antenna_coords:
        for v in range(len(antenna_coords[key])):
            x, y = antenna_coords[key][v]
            antenna = antenna_coords[key]
            for z in antenna:
                if z == (x, y):
                    continue
                a, b = z
                x_dist, y_dist = a - x, b - y
                x2 = a + x_dist
                y2 = b + y_dist
                part2_antinode_coords.add((a, b))

                if x2 < len(grid) and y2 < len(grid[0]) and x2 >= 0 and y2 >= 0:
                    part1_antinode_coords.add((x2, y2))

                while x2 < len(grid) and y2 < len(grid[0]) and x2 >= 0 and y2 >= 0:
                    part2_antinode_coords.add((x2, y2))
                    x2 = x2 + (a - x)
                    y2 = y2 + (b - y)

    return (len(part1_antinode_coords), len(part2_antinode_coords))


if __name__ == "__main__":
    with open("input/day8.txt") as f:
        grid = [list(x.rstrip()) for x in f]

    antenna_coords = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            char_at = grid[i][j]
            if char_at != "." and char_at != "#":
                antenna_coords[char_at].append((i, j))

    result = solve(antenna_coords)
    print(result[0])
    print(result[1])
