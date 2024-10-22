"""
Pathfinding With Obstacles
Problem: Extend the previous problem by adding obstacles to the grid (cells that are impassable).
Goal: Learn how to handle grids where not all nodes are accessible. A* should find a way around obstacles.
Heuristic: Continue to use the Manhattan distance for the heuristic.
"""
import heapq
import math

# Manhatten Distance as heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Cost as euclidian distance
def cost(a, b):
    result = (a[0] - b[0])**2 + (a[1] - b[1])**2
    return math.sqrt(result)

# Trying to get all eight neighbors of the given node in given grid.
def get_all_neighbors(grid, node):
    neighbors = []
    x, y = node

    # Verticle and Horizontal Neighbors
    if x > 0: neighbors.append((x-1, y))
    if x < len(grid) - 1: neighbors.append((x+1, y))
    if y > 0: neighbors.append((x, y-1))
    if y < len(grid[0])-1 : neighbors.append((x, y+1))

    # Diagonal Neighbors
    if x > 0 and y < len(grid[0]) -1: neighbors.append((x-1, y+1))
    if x > 0 and y > 0: neighbors.append((x-1, y-1))
    if x < len(grid) - 1 and y < len(grid[0]) -1: neighbors.append((x+1, y+1))
    if x < len(grid) - 1 and y > 0: neighbors.append((x+1, y-1))

    return neighbors

# Finally searching path using A* Star and above defined functions
def A_star(grid, start, target):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_score = {start : 0}
    f_score = {start : heuristic(start, target)}

    node_predecessor = {}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == target: # when target is found.
            path = []
            while current in node_predecessor:
                path.append(current)
                current = node_predecessor[current]
            path.append(start)
            return path[::-1] # reversing the path

        for neighbor in get_all_neighbors(grid, current):
            if grid[neighbor[0]][neighbor[1]] != 1: # Avoiding obstacles
                tentative_g_score = g_score[current] + cost(current, neighbor)
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    node_predecessor[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, target) # dist(current, neighbor) + heuristic_dist(neighbor, target)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return f"There is no path from {start} to {target} in given grid."
#-------------------------------------------------------------
#-------------------------------------------------------------
grid = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
]

start_position = (0, 2)
target_position = (6, 9)

resultant_path = A_star(grid, start=start_position, target=target_position)
print(resultant_path)

# result = get_all_neighbors(grid, (1, 8))
# print(result)