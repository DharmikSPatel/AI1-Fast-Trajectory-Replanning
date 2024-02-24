from maze import Maze
from A_star import repeated_a_star

'''print("Maze 0") 
maze0 = Maze(size=10)
maze0.print_maze()
print("Forwards Repeated A* took:", repeated_a_star(maze0))
maze0.print_maze()
maze0.reset_maze()
print("Backwards Repeated A* took:", repeated_a_star(maze0, backwards=True))
maze0.print_maze()
print()'''


'''print("Maze 1")
maze1 = Maze.load_maze('mazes/maze1.txt')
maze1.print_maze()
print("Forwards Repeated A* took:", repeated_a_star(maze1))
maze1.print_maze()
maze1.reset_maze()
print("Backwards Repeated A* took:", repeated_a_star(maze1, backwards=True))
maze1.print_maze()
maze1.reset_maze()
print("Adaptive Repeated A* took:", repeated_a_star(maze1, adaptive=True))
maze1.print_maze()
print()'''


'''print("Maze 2")
maze2 = Maze.load_maze('mazes/maze2.txt')
maze2.print_maze()
print("Forwards Repeated A* took:", repeated_a_star(maze2))
# maze2.print_maze()
maze2.reset_maze()
print("Backwards Repeated A* took:", repeated_a_star(maze2, backwards=True))
# maze2.print_maze()
maze2.reset_maze()
print("Adaptive Repeated A* took:", repeated_a_star(maze2, adaptive=True))
# maze2.print_maze()
print()'''

for i in range(50):
    maze = Maze.generate_maze(101)
    print(i + 1)
    maze.print_maze()
    print()
    print("Forwards Repeated A* took:", repeated_a_star(maze))
    maze.print_maze()
    maze.reset_maze()
    print("Backwards Repeated A* took:", repeated_a_star(maze, backwards=True))
    maze.print_maze()
    maze.reset_maze()
    print("Adaptive Repeated A* took:", repeated_a_star(maze, adaptive=True))
    maze.print_maze()
    print()


# print("Maze 3")
# maze3 = Maze.load_maze('mazes/maze3.txt')
# maze3.print_maze()
# print("Forwards Repeated A* took:", a_star(maze3))
# # maze3.print_maze()
# maze3.reset_maze()
# print("Backwards Repeated A* took:", a_star(maze3, backwards=True))
# # maze3.print_maze()
# maze3.reset_maze()
# print("Adaptive Repeated A* took:", a_star(maze3, adaptive=True))
# # maze3.print_maze()
# print()

