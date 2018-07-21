# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = [4, 3, 1, 2, 0]
    insertionsort(arr)
    assert arr == [0, 1, 2, 3, 4]
