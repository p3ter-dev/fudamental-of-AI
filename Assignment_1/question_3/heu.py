import heapq
import matplotlib.pyplot as plt
import networkx as nx
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
            popped_item = heapq.heappop(priority_queue)
            g = popped_item[1]
            current_node = popped_item[2]           
            path = popped_item[3]             
            if current_node in visited:
                continue
                
            visited.add(current_node)

            if current_node == goal:
                return path, g
            
            for neighbor, cost in self.graph.get(current_node, []):
                if neighbor in visited:
                    continue
                heuristic_value = self.heuristic.get(neighbor, float('inf'))
                new_g = g + cost
                if neighbor not in cost_so_far or new_g < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_g
                    new_f = new_g + heuristic_value
                    heapq.heappush(priority_queue, (new_f, new_g, neighbor, path + [neighbor]))
        
        return None, float('inf')

G = nx.Graph()

for node, neighbors in graph.items():
    if node in heuristics:
        G.add_node(node, heuristics=heuristics[node])

for node1, neighbors in graph.items():
    for node2, cost in neighbors:
        G.add_edge(node1, node2, weight=cost)

plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='skyblue')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.7, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

node_labels = nx.get_node_attributes(G, 'heuristics')
for node, label in node_labels.items():
    x, y = pos[node]
    plt.text(x, y + 0.05, str(label), fontsize=10, ha='center', color='red')

plt.title('Graph of Ethiopian Cities with Heuristics and Edge Costs')
plt.axis('off')
plt.show()
a_star = AstarSearch(graph, heuristics)
path, cost = a_star.search("Addis Ababa", "Moyale")
print("Optimal Path:", " → ".join(path))
print("Total Cost:", cost)
print("Number of cities visited:", len(path))