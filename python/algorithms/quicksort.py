# Quick Sort
# Time Complexity O(n log(n))
# Space Complexity O(1)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


if __name__ == '__main__':
    x = [1, 3, 6, 9, 4, 2]
    quicksort(x, 0, len(x) - 1)
    assert x == [1, 2, 3, 4, 6, 9]
