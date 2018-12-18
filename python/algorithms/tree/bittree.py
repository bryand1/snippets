# https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/


def getsum(bittree, i):
    s = 0
    i = i + 1
    while i > 0:
        s += bittree[i]
        i -= i & (-i)
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
    # for i in range(0,n+1): 
    #     print(bittree[i], end=' ')
    return bittree


if __name__ == '__main__':
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    bittree = construct(freq)
