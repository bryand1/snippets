# Breadth-first search
from collections import deque


def breadth_first_search(graph, start, goal):
    frontier = deque()
    frontier.appendleft(start)
    came_from = {}
    came_from[start] = None
    while frontier:
        current = frontier.pop()
        if current == goal:
            break
        for n in graph.neighbors(current):
            if n not in came_from:
                frontier.appendleft(n)
                came_from[n] = current
    return came_from

