
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
    key_position = {}
    x,y= len(data),len(data[0])
    for row in range(x):
        for col in range(y):
            cell = data[row][col]
            if cell == "@":
                robots.append((row,col))
            elif cell in keys_char:
                key_position[(row, col)] = cell

    all_keys = set(key_position.values())

    points = robots[:]
    for coord in key_position:
        points.append(coord)

    quantity = len(points)
    distance = [dict() for _ in range(quantity)]

    def bfs(point):
        points_x, points_y = points[point]
        queue = collections.deque([point])
        queue.append((points_x, points_y, 0, set()))
        visited = {(points_x, points_y)}


def main():
    data = get_input()
    result = min_steps_to_collect_all_keys(data)
    print(result)


if __name__ == '__main__':
    main()