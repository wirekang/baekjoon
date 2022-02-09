n, m = map(int, input().split())
picked = []  # type: list[int]


def fun(level: int):
    if level == m:
        for p in picked:
            print(p, "", end="")
        print()
        return

    for i in range(1, n+1):

        picked.append(i)
        fun(level+1)
        picked.pop()


fun(0)
