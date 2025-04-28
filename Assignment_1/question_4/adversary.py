import networkx as nx
import matplotlib.pyplot as plt

from graph import graph
from utilities import utilities
class MiniMaxAgent:
    def __init__(self, graph, utilities):
        self.graph = graph
        self.utilities = utilities
    
    def minimax(self, current, depth, is_maximizing):
        if current not in self.graph or not self.graph[current]:
            return self.utilities.get(current, 0), current

        if depth == 0:
            return self.utilities.get(current, 0), current

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for neighbor in self.graph[current]:
                eval, _ = self.minimax(neighbor, depth-1, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = neighbor
            return max_eval, best_move

        else:
            min_eval = float('inf')
            worst_move = None
            for neighbor in self.graph[current]:
                eval, _ = self.minimax(neighbor, depth-1, True)
                if eval < min_eval:
                    min_eval = eval
                    worst_move = neighbor
            return min_eval, worst_move

    def find_best_path(self, start, max_depth):
        value, best_move = self.minimax(start, max_depth, True)
        return best_move, value


def plot_graph(graph):
    G = nx.DiGraph()
    
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
    
    plt.title("Graph Visualization in adversarial search")
    plt.show()

plot_graph(graph)

agent = MiniMaxAgent(graph, utilities)
best_city, best_value = agent.find_best_path('Addis Ababa', 3)
print(f"Best move is to go to {best_city} with utility {best_value}")