class MinMax:
    def __init__(self, graph, utilities, initial_state):
        self.graph = graph
        self.utilities = utilities
        self.initial_state = initial_state

    def is_terminal(self, state):
        return state in self.utilities
    

    def minmax(self, state, is_max_player):
        if self.is_terminal(state):
            return self.utilities[state], state
        
        best_value = float('-inf') if is_max_player else float('inf')
        best_path = []

        for child in self.graph.get(state, []):
            value, path = self.minmax(child, not is_max_player)
            if is_max_player:
                if value > best_value:
                    best_value = value
                    best_path = [state] + path
            else:
                if value < best_value:
                    best_value = value
                    best_path = [state] + path

        return best_value, best_path
    
    def get_best_path(self):
        value, path = self.minmax(self.initial_state, True)
        return value, path