from collections import deque
from graph_conversion import graph
class Search:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal, strategy='bfs'):
        if strategy not in ('bfs', 'dfs'):
            raise ValueError("Strategy must be either 'bfs' or 'dfs'.")

        if strategy == 'bfs':
            frontier = deque([[start]])
        else:
            frontier = [[start]]

        explored = set()

        while frontier:
            if strategy == 'bfs':
                path = frontier.popleft()
            else:
                path = frontier.pop()

            current_node = path[-1]

            if current_node == goal:
                return path

            if current_node not in explored:
                explored.add(current_node)

                for neighbor in self.graph.get(current_node, []):
                    if neighbor not in explored:
                        new_path = path + [neighbor]
                        frontier.append(new_path)
        return None


searcher = Search(graph)

print(searcher.search('Addis Ababa', 'Moyale', strategy='bfs'))

print(searcher.search('Addis Ababa', 'Moyale', strategy='dfs'))