from collections import deque

class Search:
    def __init__(self, graph):
        self.graph = graph
    
    def bfs(self, start_node, goal_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            path = queue.popleft()
            city = path[-1]

            if city == goal_node:
                return path
            
            if city not in visited:
                visited.add(city)
                for neighbor in self.graph.get(city, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None
    
    def dfs(self, start_node, goal_node):
        visited = set()
        stack = [[start_node]]

        while stack:
            path = stack.pop()
            city = path[-1]

            if city == goal_node:
                return path
            
            if city not in visited:
                visited.add(city)
                for neighbor in self.graph.get(city, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
        return None
    
    def search(self, start_node, goal_node, method='bfs'):
        if method == 'bfs':
            return self.bfs(start_node, goal_node)
        elif method == 'dfs':
            return self.dfs(start_node, goal_node)
        else:
            raise ValueError("Method must be 'bfs' or 'dfs'")


ethipian_search_graph = {
    'Addis Ababa': ['Debre Zeit', 'Ambo'],
    'Debre Zeit': ['Addis Ababa', 'Adama'],
    'Ambo': ['Addis Ababa', 'Nekemte'],
    'Adama': ['Debre Zeit', 'Assela'],
    'Assela': ['Adama'],
    'Nekemte': ['Ambo']
}

problem = Search(ethipian_search_graph)

print("BFS Path: ", problem.search('Adama', 'Nekemte', method='bfs'))
print("DFS Path: ", problem.search('Adama', 'Nekemte', method='dfs'))