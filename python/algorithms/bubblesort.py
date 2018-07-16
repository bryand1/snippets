# Bubble Sort
# Time complexity: O(n^2)
# Space complexity: O(1)


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = [4, 3, 1, 2, 0]
    bubblesort(arr)
    assert arr == [0, 1, 2, 3, 4]
