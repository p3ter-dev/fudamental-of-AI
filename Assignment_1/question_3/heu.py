import heapq

class AstarSearch:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
    
    def search(self, start, goal):

        priority_queue = [(self.heuristic[start], 0, start, [start])]
        visited = set()

        while priority_queue:
            f, g, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == goal:
                return path, g
            
            for neighbor, cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    new_g = g + cost
                    new_f = new_g + self.heuristic[neighbor]
                    heapq.heappush(priority_queue, (new_f, new_g, neighbor, path + [neighbor]))
        
        return None, float('inf')

        