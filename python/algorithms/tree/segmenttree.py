from sys import maxsize

minsize = -99999

def maxquery(segtree, qlo, qhi, lo, hi, pos):
    if qlo <= lo and qhi >= hi:
        return segtree[pos]
    if qlo > hi or qhi < lo:
        return minsize
    mid = (lo + hi) // 2
    return max(
        maxquery(segtree, qlo, qhi, lo, mid, 2 * pos + 1),
        maxquery(segtree, qlo, qhi, mid + 1, hi, 2 * pos + 2))

def construct(arr, segtree, lo, hi, pos):
    if lo == hi:
        segtree[pos] = arr[lo]
        return
    mid = (lo + hi) // 2
    construct(arr, segtree, lo, mid, 2 * pos + 1)
    construct(arr, segtree, mid + 1, hi, 2 * pos + 2)
    segtree[pos] = max(segtree[2 * pos + 1], segtree[2 * pos + 2])

if __name__ == '__main__':
    A = [-1, 0, 3, 2, 5]
    tree = [minsize] * 2 * (len(A))
    construct(A, tree, 0, len(A) - 1, 0)
    print(maxquery(tree, 2, 4, 0, 4, 0))
    print(tree)
