def check_index(index, a, b):
    return a <= index <= b


def all_path_between_lines(above_line, below_line, all_path, k):
    new_all_path = []
    for i, arr in enumerate(all_path):
        el_index = above_line.index(arr[-1])
        for dif_k in range(-k, k + 1):
            if check_index(dif_k + el_index, 0, len(below_line) - 1):
                new_all_path.append(
                    all_path[i] + [below_line[dif_k + el_index]])

    return new_all_path


def min_down_path(a, max_diff):
    all_path = [[el] for el in a[0]]
    for i in range(len(a) - 1):
        all_path = all_path_between_lines(a[i], a[i+1], all_path, max_diff)

    min_sum = None
    for arr in all_path:
        if min_sum is None or sum(arr) < min_sum:
            min_sum = sum(arr)

    return min_sum


def main():
    max_diff = int(input())
    n = int(input())
    a = []

    for _ in range(n):
        m = int(input())
        line = []
        if m != 0:
            line = list(map(int, input().split()))
        a.append(line)

    for arr in a:
        if len(arr) == 0:
            print(-1)
            return

    print(min_down_path(a, max_diff))


if __name__ == "__main__":
    main()
