from maze import Maze

blankmaze = Maze(size=10)
blankmaze.print_maze()

maze1 = Maze.load_maze('mazes/maze1.txt')
maze1.print_maze()