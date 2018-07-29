# Depth-first search
# Time complexity O(V + E), when implemented using the adjacency list.


def dfs_iterative(graph, start):
    path = []
    st = [start]
    visited = {start}
    while st:
        v = st.pop()
        path.append(v)
        for u in graph[v]:
            if u not in visited:
                st.append(u)
                visited.add(u)
    return path


def dfs_recursive(graph, vertex, path=[]):
    path.append(vertex)
    for v in graph[vertex]:
        if v not in path:
            dfs_recursive(graph, v, path)
    return path


if __name__ == '__main__':
    g = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: []
    }
    print(dfs_iterative(g, 1))
    print(dfs_recursive(g, 1))
