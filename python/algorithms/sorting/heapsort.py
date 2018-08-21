def maxheapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxheapify(arr, n, largest)


def minheapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minheapify(arr, n, smallest)


def heapsort(arr, reverse=False):
    heapify = minheapify if reverse else maxheapify
    n = len(arr)
    for i in range(n - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':
    x = [12, 11, 13, 5, 6, 7]
    heapsort(x, reverse=True)
    print("Sorted array is: ")
    print(x)
