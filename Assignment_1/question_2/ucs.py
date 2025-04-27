import heapq
from graph_conversion import graph
def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))
    cost_so_far = {start: 0}
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, cost

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float('inf')

path, total_cost = uniform_cost_search(graph, 'Addis Ababa', 'Lalibela')
print("Path:", path)
print("Total Cost:", total_cost)