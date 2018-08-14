def binary_search(A, x):

    # Initialize search region to the entire array
    # [lo, hi)

    lo, hi = 0, len(A)

    while hi - lo > 1:
        mid = (hi + lo) // 2
        if x < A[mid]:
            hi = mid
        elif x == A[mid]:
            return True
        else:  # x > A[mid]
            lo = mid + 1

    if lo == hi:
        return False
    else:
        return x == A[lo]
