import networkx as nx
import matplotlib.pyplot as plt

from collections import deque
from graph_conversion import graph
class Search:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal, strategy='bfs'):
        if strategy not in ('bfs', 'dfs'):
            raise ValueError("Strategy must be either 'bfs' or 'dfs'.")
        
        print(f"Searching from {start} to {goal} using {strategy.upper()} strategy.")

        if strategy == 'bfs':
            paths_to_explore = deque([[start]])
        else:
            paths_to_explore = [[start]]

        explored = set()

        while paths_to_explore:
            if strategy == 'bfs':
                path = paths_to_explore.popleft()
            else:
                path = paths_to_explore.pop()

            current_node = path[-1]

            if current_node == goal:
                return path

            if current_node not in explored:
                explored.add(current_node)

                for neighbor in self.graph.get(current_node, []):
                    if neighbor not in explored:
                        new_path = path + [neighbor]
                        paths_to_explore.append(new_path)
        return None

G = nx.Graph()

for node, edges in graph.items():
    for neighbor in edges:
        G.add_edge(node, neighbor)

plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='skyblue')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.7, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

plt.title('Graph of Ethiopian Cities based on the given graph')
plt.axis('off')
plt.show()
searcher = Search(graph)

print(searcher.search('Addis Ababa', 'Moyale', strategy='bfs'))

print(searcher.search('Addis Ababa', 'Moyale', strategy='dfs'))