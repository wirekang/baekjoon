n, m = map(int, input().split())

picks = []  # type: list[int]
checks = [False]*(n+1)

rst = set()  # type: set[str]


def f(count: int):
    if count == m:
        c = picks.copy()
        c.sort()
        rst.add(' '.join(list(map(str, c))))

    for i in range(1, n+1):
        if checks[i]:
            continue

        checks[i] = True
        picks.insert(0, i)
        f(count+1)
        checks[i] = False
        picks.pop(0)


f(0)

l = list(rst)
l.sort()
for s in l:
    print(s)
