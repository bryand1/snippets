# Selection Sort
# Time Complexity O(n^2)
# Space Complexity O(1)


def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        m = i
        for j in range(i, n):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]


if __name__ == '__main__':
    arr = [9, 8, 7, 1, 2, 3]
    selectionsort(arr)
    assert arr == [1, 2, 3, 7, 8, 9]
