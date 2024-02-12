from maze import Maze

maze1 = Maze()
maze1.print_maze()

maze2 = Maze(Maze.LOAD_MAZE, maze_txt='mazes/maze1.txt')
maze2.print_maze()