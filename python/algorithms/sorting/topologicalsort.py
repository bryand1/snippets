from collections import deque


def topologicalsort(dag):
    in_degree = {u: 0 for u in dag}
    for u in dag:
        for v in dag[u]:
            in_degree[v] += 1
    q = deque()
    for u in in_degree:
        if in_degree[u] == 0:
            q.appendleft(u)
    t = []
    while q:
        u = q.pop()
        t.append(u)
        for v in dag[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.appendleft(v)
    if len(t) == len(dag):
        return t
    else:
        raise ValueError('graph is not acyclic')


if __name__ == '__main__':
    graph = {
        1: [2, 3],
        2: [3, 4],
        3: [4, 5],
        4: [],
        5: [],
    }
    t = topologicalsort(graph)
    print(t)

