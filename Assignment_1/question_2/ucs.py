import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return path + [node], cost
        if node not in visited:
            continue
        visited.add(node)

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [node]))
    return None, float('inf')
