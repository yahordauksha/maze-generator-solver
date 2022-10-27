import random


passage_cell_height = 5
passage_cell_width = 0
height = 10
width = 20

maze = []


def empty_maze_generator(height, width):
    for i in range(height):
        line = []
        for x in range(width):
            line.append(2)
        maze.append(line)
    return maze


# Checking what cells to turn to walls next to curent cell
# then randomly choosing which one to turn into passageway
# then running the function again, changing curent cell to the random wall
def check_for_walls(passage_cell_height, passage_cell_width, maze):
    print('\n')
    print("Check for walls wtarts with parametres: ",
          passage_cell_height, passage_cell_width)
    walls = []

    maze[passage_cell_height][passage_cell_width] = 0
    # Checking wall under the cell
    if passage_cell_height + 1 <= height and maze[passage_cell_height + 1][passage_cell_width] == 2:
        maze[passage_cell_height + 1][passage_cell_width] = 1
        wall = [passage_cell_height + 1, passage_cell_width]
        walls.append(wall)

    # Checking wall above the cell
    if passage_cell_height - 1 >= 0 and passage_cell_height + 1 >= 0 and maze[passage_cell_height - 1][passage_cell_width] == 2:
        maze[passage_cell_height - 1][passage_cell_width] = 1
        wall = [passage_cell_height - 1, passage_cell_width]
        walls.append(wall)

    # Checking wall to the right of the cell
    if passage_cell_width + 1 <= width and maze[passage_cell_height][passage_cell_width + 1] == 2:
        maze[passage_cell_height][passage_cell_width + 1] = 1
        wall = [passage_cell_height, passage_cell_width + 1]
        walls.append(wall)

    # Checking wall to the left of the cell
    if passage_cell_width - 1 >= 0 and maze[passage_cell_height][passage_cell_width - 1] == 2:
        maze[passage_cell_height][passage_cell_width - 1] = 1
        wall = [passage_cell_height, passage_cell_width - 1]
        walls.append(wall)

    print("Walls contain: ", walls)
    passage_cells = random.choice(walls)
    passage_cell_height = passage_cells[0]
    passage_cell_width = passage_cells[1]

    print("New passage cell height: ", passage_cell_height)
    print("New passage cell width: ", passage_cell_width)

    # return passage_cell_height, passage_cell_width, maze
    print_maze(maze)
    check_for_walls(passage_cell_height, passage_cell_width, maze)


# Maze output to the command line


def print_maze(maze):
    print("----------------------------------")
    for i in range(0, len(maze)):

        for j in range(0, len(maze[0])):
            print(maze[i][j], end=" ")

        print('\n')
    print("----------------------------------")


empty_maze_generator(height, width)

check_for_walls(passage_cell_height, passage_cell_width, maze)
