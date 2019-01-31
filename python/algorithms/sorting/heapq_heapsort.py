from heapq import heappush, heappop


def heapsort(arr):
    h = []
    for i in arr:
        heappush(h, i)
    return [heappop(h) for i in range(len(h))]


if __name__ == '__main__':
    a = [3, 1, 7, 6, 9, 0]
    s = heapsort(a)
    print(s)
