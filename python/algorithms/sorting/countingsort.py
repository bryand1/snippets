def countingsort(arr):
    ret = []
    k = max(arr) + 1
    aux = [0] * k
    for num in arr:
        aux[num] += 1
    for i in range(k):
        tmp = aux[i]
        while tmp:
            ret.append(i)
            tmp -= 1
    return ret


if __name__ == '__main__':
    x = [3, 1, 0, 6, 7, 5, 7]
    print(countingsort(x))
