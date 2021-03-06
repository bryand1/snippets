# https://www.python.org/doc/essays/graphs/


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if shortest is None or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

