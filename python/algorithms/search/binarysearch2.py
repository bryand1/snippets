def recursive(A, l, r, x):
    if l <= r:
        mid = (l + r) // 2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return recursive(A, l, mid - 1, x)
        else:
            return recursive(A, mid + 1, r, x)
    else:
        return -1

def iterative(A, x):
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def helper(result):
    if result != -1: 
        print("Element is present at index % d" % result)
    else: 
        print("Element is not present in array")


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40] 
    x = 10
    result = recursive(arr, 0, len(arr) - 1, x) 
    helper(result)
    result = iterative(arr, x)
    helper(result)

    x = 5
    result = recursive(arr, 0, len(arr) - 1, x) 
    helper(result)
    result = iterative(arr, x)
    helper(result)

    y = []
    result = iterative(y, 2)
    helper(result)
