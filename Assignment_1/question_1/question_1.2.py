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


searcher = Search(graph)

print(searcher.search('Addis Ababa', 'Moyale', strategy='bfs'))

print(searcher.search('Addis Ababa', 'Moyale', strategy='dfs'))