from collections import deque
from copy import deepcopy


class Disk:
    def __init__(self, free: deque, files: dict, file_str: list, id_to_blocks: dict):
        self.free = free
        self.files = files
        self.file_str = file_str
        self.id_to_blocks = id_to_blocks


def read_diskmap(line: str) -> Disk:
    files = {}
    id_to_blocks = {}
    free = deque()
    file_str = []
    next_id = 0

    for i in range(len(line)):
        blocks = int(line[i])
        if i % 2 == 0:
            for _ in range(blocks):
                files[len(file_str)] = next_id
                file_str += "A"
            id_to_blocks[next_id] = blocks
            next_id += 1
        else:
            # digit indicates free space
            file_str += "." * blocks
            free.extend(range((len(file_str) - blocks), len(file_str)))

    return Disk(free, files, file_str, id_to_blocks)


def calculate_checksum(file_str: list, files: dict) -> int:
    checksum = 0
    for i in range(len(file_str)):
        if file_str[i] != ".":
            checksum += i * int(files[i])

    return checksum


def part1(disk: Disk) -> int:
    free = disk.free
    files = disk.files
    file_str = disk.file_str

    for j, e in reversed(list(enumerate(file_str))):
        if e != "." and free and len(file_str) > len(files):
            new_pos = free.popleft()
            if new_pos < j and j in files:
                curr_id = files[j]
                files[new_pos] = curr_id
                file_str[new_pos] = e
                del files[j]
                del file_str[j]

    return calculate_checksum(file_str, files)


def part2(disk: Disk) -> int:
    free = list(disk.free)
    files = disk.files
    file_str = disk.file_str
    id_to_blocks = disk.id_to_blocks

    for j, e in reversed(list(enumerate(file_str))):
        print("FOR J", j)
        if e != "." and free and j in files:
            # get ID + len of this element
            id = files[j]
            blocks = id_to_blocks[id]

            # find a contiguous set of indices in free that can hold blocks
            for start in range(len(free) - blocks + 1):
                if all(free[start + k] == free[start] + k for k in range(blocks)):
                    # Found a block
                    new_positions = free[start : start + blocks]
                    valid_move = True
                    for k, new_pos in enumerate(new_positions):
                        if j - k <= new_pos:
                            valid_move = False
                            break
                    if valid_move:
                        for k, new_pos in enumerate(new_positions):
                            files[new_pos] = id
                            file_str[new_pos] = file_str[j - k]
                        free = free[:start] + free[start + blocks :]
                        for k in range(blocks):
                            old_pos = j - k
                            if old_pos in files:
                                del files[old_pos]
                            file_str[old_pos] = "."
                        break

    return calculate_checksum(file_str, files)


if __name__ == "__main__":
    with open("input/day9.txt") as f:
        line = f.readline().strip()
    disk = read_diskmap(line)
    print(part1(deepcopy(disk)))
    print(part2(disk))
