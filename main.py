import random
from PIL import Image

wall = 1  # Wall, white in color
space = 0  # Passage, black in color

# Random maze dimensions
height = random.randint(100, 200)
width = random.randint(100, 200)

# Random starting point
passage_cell_height = random.randint(0, height)
passage_cell_width = 0

# Lists
maze = []  # A main maze
walls_all = []  # A list of all the walls there is


# Empty maze generator (2 is an empty space, not a passage nor a wall)
def empty_maze_generator(height, width, passage_cell_height):
    for i in range(height):
        line = []
        for x in range(width):
            line.append(2)
        maze.append(line)

    passage_cell_height = random.randint(0, height)
    return maze, passage_cell_height


# prims_algorithm


# Checking what cells to turn to walls next to curent cell
# then randomly choosing which one to turn into passageway
# then running the function again, changing curent cell to the random wall
def prims_algorithm(passage_cell_height, passage_cell_width, maze, walls_all):
    print('\n')
    print("Check for walls wtarts with parametres: ",
          passage_cell_height, passage_cell_width)
    walls_temp = []

    maze[passage_cell_height][passage_cell_width] = 0
    # Checking wall under the cell
    if passage_cell_height + 1 <= height and maze[passage_cell_height + 1][passage_cell_width] == 2:
        maze[passage_cell_height + 1][passage_cell_width] = 1
        wall = [passage_cell_height + 1, passage_cell_width]
        walls_temp.append(wall)

    # Checking wall above the cell
    if passage_cell_height - 1 >= 0 and passage_cell_height + 1 >= 0 and maze[passage_cell_height - 1][passage_cell_width] == 2:
        maze[passage_cell_height - 1][passage_cell_width] = 1
        wall = [passage_cell_height - 1, passage_cell_width]
        walls_temp.append(wall)

    # Checking wall to the right of the cell
    if passage_cell_width + 1 <= width and maze[passage_cell_height][passage_cell_width + 1] == 2:
        maze[passage_cell_height][passage_cell_width + 1] = 1
        wall = [passage_cell_height, passage_cell_width + 1]
        walls_temp.append(wall)

    # Checking wall to the left of the cell
    if passage_cell_width - 1 >= 0 and maze[passage_cell_height][passage_cell_width - 1] == 2:
        maze[passage_cell_height][passage_cell_width - 1] = 1
        wall = [passage_cell_height, passage_cell_width - 1]
        walls_temp.append(wall)

    #print("Walls contain: ", walls)
    passage_cells = random.choice(walls_temp)
    passage_cell_height = passage_cells[0]
    passage_cell_width = passage_cells[1]

    #print("New passage cell height: ", passage_cell_height)
    #print("New passage cell width: ", passage_cell_width)

    print_maze(maze)
    save_maze(maze)
    prims_algorithm(passage_cell_height, passage_cell_width, maze, walls_all)


# Saving image of the maze in pbm format
def save_maze(maze):
    pixels = [255 if elem else 0 for row in maze for elem in row]
    img = Image.new("L", (len(maze[0]), len(maze)))
    img.putdata(pixels)
    img.save("image.pbm")


# Maze output to the command line
def print_maze(maze):
    print("----------------------------------")
    for i in range(0, len(maze)):

        for j in range(0, len(maze[0])):
            print(maze[i][j], end=" ")

        print('\n')
    print("----------------------------------")


empty_maze_generator(height, width, passage_cell_height)
prims_algorithm(passage_cell_height, passage_cell_width, maze, walls_all)

print_maze(maze)
