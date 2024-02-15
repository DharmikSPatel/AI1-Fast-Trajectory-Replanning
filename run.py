from maze import Maze
from A_star import a_star

print("Maze 0")
maze0 = Maze(size=10)
maze0.print_maze()
print("Forwards Repeated A* took:", a_star(maze0))
maze0.print_maze()
maze0.reset_maze()
print("Backwards Repeated A* took:", a_star(maze0, backwards=True))
maze0.print_maze()
print()


print("Maze 1")
maze1 = Maze.load_maze('mazes/maze1.txt')
maze1.print_maze()
print("Forwards Repeated A* took:", a_star(maze1))
maze1.print_maze()
maze1.reset_maze()
print("Backwards Repeated A* took:", a_star(maze1, backwards=True))
maze1.print_maze()
print()


print("Maze 2")
maze2 = Maze.load_maze('mazes/maze2.txt')
maze2.print_maze()
print("Forwards Repeated A* took:", a_star(maze2))
# maze2.print_maze()
maze2.reset_maze()
print("Backwards Repeated A* took:", a_star(maze2, backwards=True))
# maze2.print_maze()
print()


