from maze import Maze
from A_star import repeated_a_star

with open("Demo Output", 'w', encoding='utf-8') as f2:
    print("Demo Maze")
    f2.write("Demo Maze\n")
    maze = Maze.generate_maze(101)

    maze.print_maze()
    maze.export_maze(f2)

    temp = repeated_a_star(maze, max_num_of_steps_to_print=5, f=f2)
    print("Forwards Repeated A* took:", str(temp))
    f2.write("Forwards Repeated A* took: " + str(temp) + "\n")
    maze.print_maze()
    maze.export_maze(f2)

    maze.reset_maze()
f2.close()

# Terminal Can't Save all this (not on PyCharm at least)
# Need to export to a txt file to read full thing

# TODO
# 3 algos: forward, backwards, adaptive
# 2 tie/per algo: favor higher g values, or favor lower g values


with open("50 Mazes Report Output", 'w', encoding='utf-8') as f:
    for i in range(50):
        maze = Maze.generate_maze(101)

        f.write("Maze Number: " + str((i + 1)) + "\n")
        f.flush()

        temp = repeated_a_star(maze)
        f.write("Forwards Repeated A* took: " + str(temp) + "\n")
        f.flush()
        maze.reset_maze()

        temp = repeated_a_star(maze, backwards=True)
        f.write("Backwards Repeated A* took: " + str(temp) + "\n")
        f.flush()
        maze.reset_maze()

        temp = repeated_a_star(maze, adaptive=True)
        f.write("Adaptive Repeated A* took: " + str(temp) + "\n")
        f.flush()

        f.write("\n")
        f.flush()
f.close()