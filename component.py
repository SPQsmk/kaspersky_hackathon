import sys


matrix = []
mns = 0

for line in sys.stdin:
    ln = []
    for c in line:
        if c in ['0', '1']:
            if c == '0':
                mns += 1
            ln.append(int(c))
    if len(ln) > 0:
        matrix.append(ln)

mtr = []
for i in range(len(matrix) * len(matrix[0])):
    line = []
    for j in range(len(matrix) * len(matrix[0])):
        line.append(0)
    mtr.append(line)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if (j + 1) < len(matrix[0]) and matrix[i][j] == 1 and matrix[i][j + 1] == 1:
            mtr[i * len(matrix[0]) + j][i * len(matrix[0]) + j + 1] = 1
            mtr[i * len(matrix[0]) + j + 1][i * len(matrix[0]) + j] = 1
        if (i + 1) < len(matrix) and matrix[i][j] == 1 and matrix[i + 1][j] == 1:
            mtr[i * len(matrix[0]) + j][(i + 1) * len(matrix[0]) + j] = 1
            mtr[(i + 1) * len(matrix[0]) + j][i * len(matrix[0]) + j] = 1

size = len(mtr)
adj_list = []
for i in range(size):
    lst = []
    for j in range(size):
        if mtr[i][j] == 1:
            lst.append(j)
    adj_list.append(lst)

visited = [False] * size


def dfs(x):
    visited[x] = True
    for w in adj_list[x]:
        if not visited[w]:
            dfs(w)


ans = 0
for v in range(size):
    if not visited[v]:
        dfs(v)
        ans += 1

print(ans - mns)
