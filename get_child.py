in_str = input()


def get_child(parents, length):
    if length == 1:
        return parents[0]

    for i in range(length - 1):
        parents[i] = child(parents[i], parents[i + 1])

    return get_child(parents, length - 1)


def child(a, b):
    if a == b:
        return a
    elif a == 'A' and b == 'B' or a == 'B' and b == 'A':
        return 'C'
    elif a == 'A' and b == 'C' or a == 'C' and b == 'A':
        return 'B'
    else:
        return 'A'


p = [x for x in in_str]
res = get_child(p, len(p))
print(res)
