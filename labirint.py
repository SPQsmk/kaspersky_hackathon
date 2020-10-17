import numpy as np


def get_coords(m, x, y, k):
    if m[x][y] == 1:
        y -= k
        x += k
    elif m[x][y] == 2:
        x += k
    elif m[x][y] == 3:
        y += k
        x += k
    elif m[x][y] == 4:
        y -= k
    elif m[x][y] == 6:
        y += k
    elif m[x][y] == 7:
        y -= k
        x -= k
    elif m[x][y] == 8:
        x -= k
    elif m[x][y] == 9:
        y += k
        x -= k
    return x, y


def check_index(index, a, b):
    return a <= index <= b


def get_path(m, x, y, path, all_paths):
    if m[x][y] == 5:
        all_paths.append(path)
        return

    if (x, y) in path[:-1]:
        return

    for k in range(1, len(m)):
        p_i, p_j = get_coords(m, x, y, k)
        if check_index(p_i, 0, len(m) - 1) and check_index(p_j, 0, len(m) - 1):
            get_path(m, p_i, p_j, path + [(p_i, p_j)], all_paths)


def to_str(path):
    ss = ''
    for (p_i, p_j) in path:
        ss += '({0}, {1});'.format(p_i, p_j)
    return ss


inp = [int(x) for x in input()]

size = inp[0]
i = inp[1]
j = inp[2]

_map = np.resize(np.array(inp[3:]), (size, size))

all_path = []
get_path(_map, i, j, [], all_path)

len_arr = [len(arr) for arr in all_path]
min_len = min(len_arr)
min_path = all_path[len_arr.index(min_len)]

print(to_str(min_path))
