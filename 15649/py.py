n, m = map(int, input().split())
picked = []  # type: list[int]
check = [False]*(n+1)  # type: list[bool]


def fun(level: int):
    if level == m:
        for p in picked:
            print(p, "", end="")
        print()
        return

    for i in range(1, n+1):
        if check[i]:
            continue

        check[i] = True
        picked.append(i)
        fun(level+1)
        check[i] = False
        picked.pop()


fun(0)
