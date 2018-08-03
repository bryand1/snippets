# Djikstra's algorithm
import heapq


class PriorityQueue:

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item):
        heapq.heappush(self.elements, item)

    def get(self):
        return heapq.heappop(self.elements)[1]


def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for node in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, node)
            if node not in cost_so_far or new_cost < cost_so_far[node]:
                cost_so_far[node] = new_cost
                priority = new_cost
                frontier.put((priority, node))
                came_from[node] = current
    return came_from, cost_so_far
