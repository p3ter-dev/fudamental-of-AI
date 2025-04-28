import heapq
import matplotlib.pyplot as plt
import networkx as nx
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

G = nx.Graph()

for node, edges in graph.items():
    for neighbor, weight in edges:
        G.add_edge(node, neighbor, weight=weight)

plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='skyblue')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.7, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('Graph of Ethiopian Cities considering their costs')
plt.axis('off')
plt.show()
path, total_cost = uniform_cost_search(graph, 'Addis Ababa', 'Lalibela')
print("Path:", path)
print("Total Cost:", total_cost)