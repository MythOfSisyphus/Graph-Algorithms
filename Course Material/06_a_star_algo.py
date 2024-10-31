"""
A* Algorithm: is very similiar to Dijkstra Algorithm(DA), if you know how DA works then you can
easily understand the current algorithm. What differentiate A* from DA is its `heuristic function`
in DA we keep track of cost of getting to current node from start node and keep searching the shortest
path by exploring all neighbors of the current node. Now A* also does this but it also try to guess how
much it would cost us to go to target node from current node.
So, here we not only push (dist, node) tuple in priority queue just by seeing its distance from start
node but (f(node), node) where f(n) = g(n) + h(n) with g(n) and h(n) are distances of current node
from start and target node respectively.

start ----g(n)-----> current -----h(n)-----> target

And we tend to visit the node which has minimum f(n) as compared to other nodes.
One commonly used heuristic function is Manhattan Distnace, which works fine for grid but not for random graphs
so always be careful with whatever heuristic function you use.

Remark: Actual tentative_g_score = g_score[current] + cost(current, neighbor),
here we have used cost(current, neighbor) = 1 because cost is acutally 1, because if you focus on how we're
getting neighbors of the current node then you can easily see this, either neighbors have x or y corrdinate
same as current node. So for weighted graph cost function can be edge weight between current and neighbor.

Try Problem 81 and 83 fo Project Euler to understand A* and tentative_g_score better.
When we need to calculate all eight neighbors, it is better to use euclidean distance as heuristic function.
(why?)
"""
import heapq

def heuristic(a, b):
    # Manhattan Distance as Heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_Star(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Dictionaries for tracking costs and paths
    g_score = {start : 0}
    f_score = {start : heuristic(start, goal)}

    came_from = {}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal: # path construction
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + 1 # See Remark above
            # if we get shorter distance then don't hesitate to update
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
                
    return None # In the case path can't be found

def get_neighbors(grid, node):
    neighbors = []
    x, y = node
    if x > 0: neighbors.append((x-1, y)) # up
    if x < len(grid) - 1: neighbors.append((x+1, y)) # down
    if y > 0: neighbors.append((x, y-1)) # left
    if y < len(grid[0]) - 1: neighbors.append((x, y+1)) # right
    return neighbors

"""
Here is more concise and efficient way to get neighbors,
it is highly efficient when we have to calculate more than
one neighbors in more than one direction.
Above code for checking each condition will get larger and larger
with so many checks and will be more error prone.
"""
def get_neighbors_2(grid, node):
    neighbors = []
    directions = [
        (-1, 0), (1, 0), # Vertical
        (0, -1, (0, 1)) # horizontal
    ]
    x, y = node
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors
#----------------------------------------------------------------------------------

grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (3, 3)

path = A_Star(grid, start, goal)
print(path)