from __future__ import annotations
class Maze:
    DEF_SIZE = 10
    BLOCKED_CELL = '#'
    FREE_CELL = '0' #if you wanna change what is printed on screen, change it in the print method
    START_CELL = 'S'
    GOAL_CELL = 'G'
    MOVED_CELL = '.'
    CARDINALS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
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
    def generate_fog_maze(self) -> Maze:
        fog_maze = Maze(size=self.size,
                    start_pos=self.start_pos, 
                    goal_pos=self.goal_pos)

        #let it know its intial neighbors
        for neighbor in self.get_neighbors(self.start_pos):
            fog_maze.set_cell(neighbor, self.get_cell(neighbor))
        return fog_maze
    @classmethod
    def generate_maze(cls, size) -> Maze:
        #return a maze
        pass
    @classmethod
    def load_maze(cls, maze_path: str) -> Maze:
        maze_file = open(maze_path)
        size = int(maze_file.readline())
        maze = Maze(size=size)

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
    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        for dx, dy in Maze.CARDINALS:
            neighbor = (x-dx, y-dy)
            if self.is_valid_pos(neighbor):
                neighbors.append(neighbor)
        return neighbors
        
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
    def move_agent_to(self, pos) -> bool:
        if not self.is_valid_pos(pos):
            return False
        if self.is_blocked(pos):
            return False
        self.agent_pos = pos
        self.set_cell(pos, Maze.MOVED_CELL)
        return True
    def is_valid_pos(self, pos) -> bool:
        x, y = pos
        return x >= 0 and x < self.size and y >= 0 and y < self.size
    def is_blocked(self, pos) -> bool:
        return self.get_cell(pos) == Maze.BLOCKED_CELL
    def is_goal(self, pos) -> bool:
        return pos == self.goal_pos
    def swap_goal_and_start(self):
        self.start_pos, self.goal_pos = self.goal_pos, self.start_pos
        self.agent_pos = self.start_pos
    def get_cell(self, pos):
        x, y = pos
        return self.maze[x][y]
    def set_cell(self, pos, value):
        x, y = pos
        self.maze[x][y] = value
    def goal_reached(self) -> bool:
        return self.agent_pos == self.goal_pos