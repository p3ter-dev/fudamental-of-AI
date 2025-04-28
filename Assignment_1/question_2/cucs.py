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

print("Path:", path)
print("Total Cost:", cost)