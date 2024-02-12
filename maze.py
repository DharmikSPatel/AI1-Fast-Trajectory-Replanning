from io import TextIOWrapper


class Maze:
    DEF_SIZE = 10
    LOAD_MAZE = 1
    GENERATE_MAZE = 2
    BLANK_MAZE = 3

    BLOCKED_CELL = '#'
    FREE_CELL = '0'
    START_CELL = 'S'
    GOAL_CELL = 'G'
    
    def __init__(self, source = BLANK_MAZE, size = DEF_SIZE, maze_txt = None) -> None:   
        self.size:int = size         
        if source == Maze.GENERATE_MAZE:
            self.maze = Maze.__generate_maze(self.size)
        elif source == Maze.LOAD_MAZE:
            maze_file = open(maze_txt)
            self.size = int(maze_file.readline())
            print("size: %d" % self.size)
            self.maze = Maze.__load_maze(self.size, maze_file)
        else:
            self.maze = [[Maze.FREE_CELL for i in range(self.size)] for j in range(self.size)]
    @classmethod
    def __generate_maze(cls, size):
        pass
    @classmethod
    def __load_maze(cls, size, maze_file: TextIOWrapper):
        lines = maze_file.read().splitlines()
        maze = [[c for c in line] for line in lines]
        maze_file.close()
        return maze
    
    def export_maze(self) -> None:
        pass
    def print_maze(self) -> None:
        # for i in range(self.size):
        #     for j in range(self.size):
        #         print_val = self.maze = 
        #         if cell == Maze.FREE_CELL:
        #             print_val = ' '
        #         print("%s " % print_val, end='')
        #     print()

        print('_%s' % ('_'*self.size*2))
        for row in self.maze:
            print("|", end='')
            for cell in row:
                print_val = cell
                if cell == Maze.FREE_CELL:
                    print_val = '0'
                print("%s " % print_val, end='')
            print("\b|")
        print('‾%s' % ('‾'*self.size*2))
        