in_str = input()
num = in_str.split(' ')
diff = []

for i in range(len(num) - 1):
    diff.append(abs(int(num[i]) - int(num[i + 1])))

res = 0
_max = 0

for i in range(len(diff)):
    res = 0
    for j in range(len(diff)):
        if diff[j] <= i + 2:
            res += 1
        if diff[j] > i + 2 and res + 1 != i + 2:
            res = 0
        elif diff[j] > i + 2 and _max < res:
            _max = res
            res = 0


if _max < res:
    _max = res

print(_max + 1)
