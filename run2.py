import sys

import collections


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def min_steps_to_collect_all_keys(data):
    robots = []
    keys_positions = {}
    x, y = len(data), len(data[0])
    for row in range(x):
        for column in range(y):
            cell = data[row][column]
            if cell == "@":
                robots.append((row, column))
            elif cell in keys_char:
                keys_positions[(row, column)] = cell

    set_keys = set(keys_positions.values())


    def bfs(start, keys):
        queue = collections.deque([(start[0], start[1], 0)])
        need_keys = []
        visited = {start}

        while queue:
            x_key, y_key, distance = queue.popleft()
            if (x_key, y_key) in keys_positions:
                key = keys_positions[(x_key,y_key)]
                if key not in keys:
                    need_keys.append((key, distance, (x_key,y_key)))
                    continue

            for dist_x, dist_y in ((1,0),(-1,0),(0,1),(0,-1)):
                next_x, next_y = x_key + dist_x, y_key + dist_y
                if (0 <= next_x < x) and (0 <= next_y < y) and (next_x, next_y) not in visited:
                    next_cell = data[next_x][next_y]
                    if next_cell == "#":
                        continue
                    if next_cell in doors_char and next_cell.lower() not in keys:
                        continue
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, distance + 1))

        return need_keys

    cache = {}

    def dfs(tuple_robots_positions, collected):
        queue = collections.deque([(tuple_robots_positions, collected, 0)])
        min_steps = None
        steps = {}

        while queue:
            robot_position, collected_keys, distance = queue.popleft()
            robots_keys = (robot_position, tuple(sorted(collected_keys)))
            if robots_keys in cache:
                continue
            if set(collected_keys) == set_keys:
                if min_steps is None or distance < min_steps:
                    min_steps = distance
                cache[robots_keys] = distance
                continue

            cache[robots_keys] = None
            for index, position in enumerate(robot_position):
                for key, dist, coordinates in bfs(position, set(collected_keys)):
                    if key in collected_keys:
                        continue
                    new_position = list(robot_position)
                    new_position[index] = coordinates
                    new_keys = collected_keys + [key]
                    new_robots_keys = (tuple(new_position), tuple(sorted(new_keys)))
                    if new_robots_keys not in steps or distance + dist < steps[new_robots_keys]:
                        steps[new_robots_keys] = distance + dist
                        queue.append((tuple(new_position), new_keys, distance + dist))

        return min_steps

    return dfs(tuple(robots), [])


def main():
    data = get_input()
    result = min_steps_to_collect_all_keys(data)
    print(result)


if __name__ == '__main__':
    main()
