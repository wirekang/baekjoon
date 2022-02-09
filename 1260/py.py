import sys


sys.setrecursionlimit(100000)
nDot, nLine, dotStart = map(int, input().split())

e = [[] for _ in range(nDot+1)]  # type: list[list[int]]

for _ in range(nLine):
    c1, c2 = map(int, input().split())
    e[c1].append(c2)
    e[c2].append(c1)
    e[c1].sort()
    e[c2].sort()

visits = [False]*(nDot+1)


def dfs(n: int):
    global visits
    global e

    if visits[n]:
        return

    visits[n] = True
    print(n, end=" ")

    for i in e[n]:
        dfs(i)


dfs(dotStart)
print()

visits = [False]*(nDot+1)

q = [dotStart]
visits[dotStart] = True


while len(q) > 0:
    n = q.pop()
    print(n, end=" ")

    for i in e[n]:
        if not visits[i]:
            visits[i] = True
            q.insert(0, i)
print()
