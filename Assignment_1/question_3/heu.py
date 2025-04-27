import heapq
from graph import graph
from heuristic_values import heuristics
class AstarSearch:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
    
    def search(self, start, goal):
        if start not in self.graph:
            raise ValueError(f"Start node '{start}' not found in graph")
        if goal not in self.heuristic:
            raise ValueError(f"Goal node '{goal}' not found in heuristics")
            
        priority_queue = [(0 + self.heuristic[start], 0, start, [start])]
        cost_so_far = {start: 0}
        visited = set()

        while priority_queue:
            _, g, current_node, path = heapq.heappop(priority_queue)
            
            if current_node in visited:
                continue
                
            visited.add(current_node)

            if current_node == goal:
                return path, g
            
            for neighbor, cost in self.graph.get(current_node, []):
                if neighbor not in self.heuristic:
                    print(f"Warning: Heuristic not found for node {neighbor} - using 0")
                    heuristic_value = 0
                else:
                    heuristic_value = self.heuristic[neighbor]
                    
                new_g = g + cost
                if neighbor not in cost_so_far or new_g < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_g
                    new_f = new_g + heuristic_value
                    heapq.heappush(priority_queue, (new_f, new_g, neighbor, path + [neighbor]))
        
        return None, float('inf')


a_star = AstarSearch(graph, heuristics)
path, cost = a_star.search("Addis Ababa", "Moyale")
print("Optimal Path:", " → ".join(path))
print("Total Cost:", cost)
print("Number of cities visited:", len(path))