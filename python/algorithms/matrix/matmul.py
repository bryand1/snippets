def matmul(X, Y):
    """Matrix multiplication O(n^3)"""
    result = [[0] * len(Y[0]) for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


if __name__ == '__main__':
    X1 = [[3, 1], [1, 0]]
    Y1 = [[2], [2]]
    print(matmul(X1, Y1))

    X2 = [[4, 0, 6], [1, 5, 2]]
    Y2 = [[2, 1], [2, 0], [2, 1]]
    print(matmul(X2, Y2))
