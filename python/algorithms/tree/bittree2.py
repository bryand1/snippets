def getsum(bittree, i):
    s = 0
    i += 1
    while i > 0:
        s += bittree[i]
        i -= i & -i
    return s

def updatebit(bittree, n, i, v):
    i += 1
    while i <= n:
        bittree[i] += v
        i += i & -i


def construct(arr):
    n = len(arr)
    bittree = [0] * (n + 1)
    for i in range(n):
        updatebit(bittree, n, i, arr[i])
    return bittree


if __name__ == '__main__':
    freq = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
    bt = construct(freq)
    print(bt)
    print(getsum(bt, 7))
