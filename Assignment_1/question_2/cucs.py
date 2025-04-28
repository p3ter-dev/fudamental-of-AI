import networkx as nx
import matplotlib.pyplot as plt
from graph_conversion import graph
from ucs import uniform_cost_search
def customized_uniform_cost_search(graph, start, goals):
    current = start
    unvisted_goals = set(goals)
    total_path = [start]
    total_cost = 0

    while unvisted_goals:
        min_cost = float('inf')
        next_goal = None
        path_to_next = []

        for goal in unvisted_goals:
            path, cost = uniform_cost_search(graph, current, goal)
            if cost < min_cost:
                min_cost = cost
                next_goal = goal
                path_to_next = path
        
        if not next_goal:
            break

        total_path += path_to_next
        total_cost += min_cost
        current = next_goal
        unvisted_goals.remove(next_goal)

    return total_path, total_cost

path, cost = customized_uniform_cost_search(graph, 'Addis Ababa',
 ['Axum', 'Gonder', 'Lalibela', 'Babile', 'Jimma', 'Bale', 'Sof Oumer', 'Arba Minch'])
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
print("Path:", path)
print("Total Cost:", cost)
