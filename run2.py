import sys

import collections


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def solve(data):
    n = len(data)
    m = len(data[0])
    robots = []
    keys = set()
    for i in range(n):
        for j in range(m):
            if data[i][j] == '@':
                robots.append((i, j))
            if data[i][j] in keys_char:
                keys.add(data[i][j])

    robots = sorted(robots)
    init = tuple(robots)

    visited, quene = {}, collections.deque()
    all_key = len(keys)

    vis_key = (init, frozenset())
    visited[vis_key] = 0

    quene.append((0, init, frozenset()))

    while quene:
        steps, position, key = quene.popleft()

        if len(key) == all_key:
            return steps

        for robot in range(4):
            x, y = position[robot]

            for sum_x, sum_y in dir:
                new_x, new_y = x + sum_x, y + sum_y

                if 0 <= new_x < n and 0 <= new_y < m:
                    symbol = data[new_x][new_y]

                    if symbol == '#':
                        continue

                    if symbol in doors_char:
                        lower_key = symbol.lower()
                        if lower_key not in key:
                            continue

                    new_key = set(key)
                    if symbol in keys_char:
                        new_key.add(symbol)
                    new_key_froze = frozenset(new_key)

                    new_pos = list(position)
                    new_pos[robot] = (new_x, new_y)
                    new_pos_sorted = tuple(sorted(new_pos))

                    new_state = (new_pos_sorted, new_key_froze)
                    new_steps = steps + 1

                    if new_state not in visited or new_steps < visited.get(new_state, float('inf')):
                        visited[new_state] = new_steps
                        quene.append((new_steps, new_pos_sorted, new_key_froze))
    return -1


def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()
