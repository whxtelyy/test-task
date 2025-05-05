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
    x,y= len(data), len(data[0])
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
            cell = data[x_key][y_key]
            if (x_key,y_key) in keys_positions:
                key = keys_positions[(x_key,y_key)]
                if key not in keys:
                    need_keys.append((key, distance, (x_key,y_key)))
                    continue

            for dist_x, dist_y in ((1,0),(-1,0),(0,1),(0,-1)):
                next_x, next_y = x + dist_x, y + dist_y
                if (0 <= next_x < x) and (0 <= next_y < y):
                    if (next_x, next_y) not in visited:
                        next_cell = data[next_x][next_y]
                        if next_cell != "#":
                            continue
                        if next_cell in doors_char and next_cell.lower() not in keys:
                            continue
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y, distance + 1,))
        return need_keys

    #тут будет подсчет шагов и поиск минимального кол-ва шагов


def main():
    data = get_input()
    result = min_steps_to_collect_all_keys(data)
    print(result)


if __name__ == '__main__':
    main()
