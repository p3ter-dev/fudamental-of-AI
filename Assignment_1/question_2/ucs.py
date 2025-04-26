import heapq
from graph_conversion import graph
def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float('inf')

path, total_cost = uniform_cost_search(graph, 'Addis Ababa', 'Adama')
print("Path:", path)
print("Total Cost:", total_cost)