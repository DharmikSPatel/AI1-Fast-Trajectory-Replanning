from __future__ import annotations
from io import TextIOWrapper
import copy
class Maze:
    DEF_SIZE = 10
    BLOCKED_CELL = '#'
    FREE_CELL = '0' #if you wanna change what is printed on screen, change it in the print method
    START_CELL = 'S'
    GOAL_CELL = 'G'
    MOVED_CELL = '.'
    #make a default blank maze
    def __init__(self, size = DEF_SIZE, start_pos=(0,0), goal_pos=None) -> None:   
        self.size:int = size
        self.start_pos:tuple = start_pos
        if goal_pos is None:
            self.goal_pos:tuple = (size-1, size-1)
        else:
            self.goal_pos:tuple = goal_pos
        self.agent_pos:tuple = start_pos
        self.maze = [[Maze.FREE_CELL for i in range(self.size)] for j in range(self.size)]
    def reset_maze(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.maze[i][j] == Maze.MOVED_CELL:
                    self.maze[i][j] = Maze.FREE_CELL
    def generate_fog_maze(self, blank_maze = False) -> Maze:
        fog_maze = Maze(size=self.size,
                    start_pos=self.start_pos, 
                    goal_pos=self.goal_pos)
        return fog_maze
    @classmethod
    def generate_maze(cls, size) -> Maze:
        #return a maze
        pass
    @classmethod
    def load_maze(cls, maze_path: str) -> Maze:
        maze_file = open(maze_path)
        size = int(maze_file.readline())
        # print(size)
        maze = Maze(size=size)

        lines = maze_file.read().splitlines()
        # print(len(lines))
        for i in range(size):
            # print(i, len(lines[i]))
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
        # print("size", self.size)
        print('_%s_' % ('_'*self.size))
        for i in range(self.size):
            print("|", end='')
            for j in range(self.size):
                print_val = self.maze[i][j]
                if print_val == Maze.FREE_CELL:
                    print_val = ' ' # change this char to change what is printed as blank space
                if (i,j) == self.start_pos:
                    print_val = Maze.START_CELL
                if (i,j) == self.goal_pos:
                    print_val = Maze.GOAL_CELL
                print("%s" % print_val, end='')
            print("|")
        print('‾%s‾' % ('‾'*self.size))
    def move_agent_to(self, new_agent_pos: tuple) -> bool:
        if not self.is_valid_pos(new_agent_pos):
            return False
        if self.maze[new_agent_pos[0]][new_agent_pos[1]] == Maze.BLOCKED_CELL:
            return False
        self.agent_pos = new_agent_pos
        self.maze[new_agent_pos[0]][new_agent_pos[1]] = Maze.MOVED_CELL
        return True
    def is_valid_pos(self, pos:tuple) -> bool:
        return pos[0] >= 0 and pos[0] < self.size and pos[1] >= 0 and pos[1] < self.size
    def is_blocked(self, x, y) -> bool:
        return self.maze[x][y] == Maze.BLOCKED_CELL
    def swap_goal_and_start(self):
        temp_pos = self.start_pos
        self.start_pos = self.goal_pos
        self.goal_pos = temp_pos
        self.agent_pos = self.start_pos