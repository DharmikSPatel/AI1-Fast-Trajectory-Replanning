from __future__ import annotations
from io import TextIOWrapper


class Maze:
    DEF_SIZE = 10
    BLANK_MAZE = 0
    BLOCKED_MAZE = 1

    BLOCKED_CELL = '#'
    FREE_CELL = '0'
    START_CELL = 'S'
    GOAL_CELL = 'G'
    #make a default blank maze or full maze
    def __init__(self, source = BLANK_MAZE, size = DEF_SIZE, start_pos=(0,0), goal_pos=(DEF_SIZE-1, DEF_SIZE-1)) -> None:   
        self.size:int = size
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        
        if source == Maze.BLANK_MAZE:
            self.maze = [[Maze.FREE_CELL for i in range(self.size)] for j in range(self.size)]
        else: #BLOCKED_MAZE
            self.maze = [[Maze.BLOCKED_CELL for i in range(self.size)] for j in range(self.size)]
    @classmethod
    def generate_maze(cls, size) -> Maze:
        #return a maze
        pass
    @classmethod
    def load_maze(cls, maze_path: str) -> Maze:
        maze_file = open(maze_path)
        size = int(maze_file.readline())

        maze = Maze(Maze.BLANK_MAZE, size=size)

        lines = maze_file.read().splitlines()
        for i in range(size):
            for j in range(size):
                cell_val = lines[i][j]
                if cell_val == maze.START_CELL:
                    maze.start_pos = (i, j)
                    cell_val = Maze.FREE_CELL
                if cell_val == maze.GOAL_CELL:
                    maze.goal_pos = (i, j)
                    cell_val = Maze.FREE_CELL  
                maze.maze[i][j] = cell_val                  
        maze_file.close()
        return maze
    
    def export_maze(self) -> None:
        pass
    def print_maze(self) -> None:
        print('_%s' % ('_'*self.size*2))
        for i in range(self.size):
            print("|", end='')
            for j in range(self.size):
                print_val = self.maze[i][j]
                if print_val == Maze.FREE_CELL:
                    print_val = '0'
                if (i,j) == self.start_pos:
                    print_val = Maze.START_CELL
                if (i,j) == self.goal_pos:
                    print_val = Maze.GOAL_CELL
                print("%s " % print_val, end='')
            print("\b|")
        print('‾%s' % ('‾'*self.size*2))
        