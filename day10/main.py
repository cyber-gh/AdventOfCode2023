import pprint


def get_possible_directions(pipe_type):
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    dx = []
    dy = []
    if pipe_type == "|":
        dx = [0, 0]
        dy = [-1, 1]
    if pipe_type == "-":
        dx = [-1, 1]
        dy = [0, 0]
    if pipe_type == "L":
        dx = [1, 0]
        dy = [0, -1]
    if pipe_type == "J":
        dx = [-1, 0]
        dy = [0, -1]
    if pipe_type == "7":
        dx = [-1, 0]
        dy = [0, 1]
    if pipe_type == "F":
        dx = [1, 0]
        dy = [0, 1]
    # S could be any of the above
    if pipe_type == "S":
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

    return dx, dy

def get_possible_neighbours(maze_input, x, y):
    dy, dx = get_possible_directions(maze_input[x][y])

    neighbours = []
    for i in range(len(dx)):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < len(maze_input) and 0 <= new_y < len(maze_input[0]):
            neighbours.append((new_x, new_y))

    return neighbours

# Now it's not that simple. Because these are pipes, it's not enough for x to be a neighbour of y, the opposite must also be true, y must be a neighbour of x.
# So we need to check if x is a neighbour of y and if y is a neighbour of x.

# We can do this by checking if x is in the neighbours of y and if y is in the neighbours of x.
def get_intersection_neighbours(maze_input, x, y):
    neighbours = get_possible_neighbours(maze_input, x, y)
    intersection_neighbours = []
    for neighbour in neighbours:
        neighbour_x, neighbour_y = neighbour
        neighbour_neighbours = get_possible_neighbours(maze_input, neighbour_x, neighbour_y)
        if (x, y) in neighbour_neighbours:
            intersection_neighbours.append(neighbour)
    return intersection_neighbours


def bfs(maze_input, visited, start_x, start_y, current_visited_marker):
    queue = [(start_x, start_y)]

    visited_nr = 0
    while queue:
        x, y = queue.pop(0)
        if visited[x][y] != 0:
            continue
        visited_nr += 1
        visited[x][y] = current_visited_marker

        for (new_x, new_y) in get_intersection_neighbours(maze_input, x, y):
            if visited[new_x][new_y] == 0:
                queue.append((new_x, new_y))
    return visited_nr


def traverse_maze(maze_input):
    n = len(maze_input)
    m = len(maze_input[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]

    current_visited_marker = 1
    ans = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                visited_nr = bfs(maze_input, visited, i, j, current_visited_marker)
                ans = max(ans, visited_nr)
                current_visited_marker += 1
    pprint.pprint(visited)
    return ans


def read_input_char_matrix():
    with open("input.txt", "r") as f:
        lines = [x.replace("\n", "") for x in f.readlines()]
        char_matrix = [list(line) for line in lines]
        return char_matrix


maze_input = read_input_char_matrix()

pprint.pprint(maze_input)

print(traverse_maze(maze_input) / 2)
