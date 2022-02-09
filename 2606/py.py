result = -1

nComputer = int(input())
nPair = int(input())

size = nComputer+1
e = [[] for i in range(size)]  # type: list[list[int]]

for _ in range(nPair):
    c1, c2 = map(int, input().split())
    e[c1].append(c2)
    e[c2].append(c1)

visited = [False]*size  # type: list[bool]


def visit(n: int):
    global result
    global visited
    global e

    if visited[n]:
        return

    visited[n] = True
    result += 1

    for i in e[n]:
        visit(i)


visit(1)

print(result)
