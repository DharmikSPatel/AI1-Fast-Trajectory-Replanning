from queue import PriorityQueue
from node import Node
import sys
import time
from maze import Maze
cardinals = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def a_star(real_maze: Maze, backwards:bool = False) -> float:
    if backwards:
        real_maze.swap_goal_and_start()
    start_time = time.time()
    fog_maze = real_maze.generate_fog_maze()
    furthest_pos = Node(fog_maze.start_pos[0], 
                        fog_maze.start_pos[1], 
                        0, 
                        h_val(fog_maze.start_pos, fog_maze.goal_pos), 
                        None)
    while real_maze.agent_pos != real_maze.goal_pos:
        computed_path:Node = compute_path(fog_maze, furthest_pos, fog_maze.goal_pos)
        traced_path:list = trace_nodes(computed_path)
        move_pos:Node
        for move_pos in traced_path:
            if real_maze.move_agent_to((move_pos.x, move_pos.y)):
                furthest_pos = Node(move_pos.x, 
                                    move_pos.y,
                                    0,
                                    h_val((move_pos.x, move_pos.y), fog_maze.goal_pos),
                                    None)
                fog_maze.move_agent_to((move_pos.x, move_pos.y))
                for dir in cardinals:
                    neighbor_x = move_pos.x - dir[0]
                    neighbor_y = move_pos.y - dir[1]
                    if real_maze.is_valid_pos(neighbor_x, neighbor_y):
                        fog_maze.maze[neighbor_x][neighbor_y] = real_maze.maze[neighbor_x][neighbor_y]
            else: #obstacle is hit
                break
    end_time = time.time()
    return end_time - start_time
def compute_path(fog_maze: Maze, start_node: Node, goal_pos: tuple) -> list:
    openlist_pq = PriorityQueue()
    openlist_map = {}

    openlist_pq.put((start_node.f_val, start_node))
    openlist_map[(start_node.x, start_node.y)] = start_node

    closedlist = []
    while openlist_pq.not_empty:
        lowest_node:Node = openlist_pq.get()[1]
        closedlist.append(lowest_node)
        if (lowest_node.x, lowest_node.y) == goal_pos:
            return lowest_node
        g_val = 1 + lowest_node.g_val
        for dir in cardinals:
            _x = lowest_node.x - dir[0]
            _y = lowest_node.y - dir[1]
            _h_val = h_val((_x, _y), goal_pos)
            node = Node(_x, _y, g_val, _h_val, lowest_node)
            if not fog_maze.is_valid_pos(node.x, node.y):
                continue
            if fog_maze.is_blocked(node.x, node.y):
                continue
            if node in closedlist:
                continue
            key = (node.x, node.y)
            if key in openlist_map: #in open list, so update it
                old_node:Node = openlist_map.get(key)
                if node.f_val < old_node.f_val:
                    old_node.f_val = node.f_val
                    old_node.g_val = node.g_val
                    old_node.parrent = node.parrent
            else:
                openlist_pq.put((node.f_val, node))
                openlist_map[key] = node
    

        

# manhattan_distance
def h_val(curr_pos: tuple, goal_pos: tuple) -> int:
    return abs(curr_pos[0] - goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])
def trace_nodes(curr_node:Node) -> list:
    if not curr_node:
        return []    
    traced_path = trace_nodes(curr_node.parrent) 
    traced_path.append(curr_node)
    return traced_path