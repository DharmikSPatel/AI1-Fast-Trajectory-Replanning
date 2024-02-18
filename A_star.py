from heapq import heappop, heappush
import time
from maze import Maze
from node import Node
h_val_dict = {}
def repeated_a_star(real_maze: Maze, backwards:bool = False, adaptive:bool = False) -> tuple[bool, float, int]:
    start_time = time.perf_counter()
    num_expanded_nodes = 0
    path_found = True
    h_val_dict.clear()
    if backwards:
        real_maze.swap_goal_and_start()
    fog_maze = real_maze.generate_fog_maze()
    while not real_maze.goal_reached():
        last_node, closed_list = a_star(fog_maze)
        num_expanded_nodes += len(closed_list)
        if last_node == None:
            path_found = False
            break
        if adaptive:
            end_g_val = last_node.g_val
            for node in closed_list:
                h_val_dict[node.pos] = end_g_val - node.g_val
        else:
            h_val_dict.clear()
        path = trace_nodes(last_node)
        for node in path:
            if real_maze.move_agent_to(node.pos):
                fog_maze.move_agent_to(node.pos)
                for neighbor in real_maze.get_neighbors(node.pos):
                    fog_maze.set_cell(neighbor, real_maze.get_cell(neighbor))
            else:
                break
    if backwards:
        real_maze.swap_goal_and_start()
    end_time = time.perf_counter()
    return(path_found, end_time - start_time, num_expanded_nodes)
def a_star(fog_maze: Maze):
    open_pq = []
    open_map = {}
    closed_set = set()
    start_node = Node(fog_maze.agent_pos, 0, h_val(fog_maze.agent_pos, fog_maze.goal_pos), None)
    heappush(open_pq, start_node)
    open_map[start_node.pos] = start_node
    while open_pq:
        min_node:Node = heappop(open_pq)
        while not min_node.active: 
            min_node = heappop(open_pq)
        if fog_maze.is_goal(min_node.pos): 
            return (min_node, closed_set)
        closed_set.add(min_node)
        for _ in fog_maze.get_neighbors(min_node.pos):
            neighbor: Node = Node(_, 1 + min_node.g_val, h_val(_, fog_maze.goal_pos), min_node)
            if fog_maze.is_blocked(neighbor.pos):
                continue
            if neighbor in closed_set:
                continue
            if neighbor.pos in open_map:
                old:Node = open_map.get(neighbor.pos)
                if neighbor.f_val < old.f_val:
                    open_map.get(neighbor.pos).active = False       
                    heappush(open_pq, neighbor)
                    open_map[neighbor.pos] = neighbor
            else:
                heappush(open_pq, neighbor)
                open_map[neighbor.pos] = neighbor
    return (None, closed_set)

def h_val(pos:tuple, goal_pos:tuple) -> int:
    if pos not in h_val_dict:
        h_val_dict[pos] = manhattan_dist(pos, goal_pos)
    return h_val_dict.get(pos)
def manhattan_dist(curr_pos: tuple, goal_pos: tuple) -> int:
    return abs(curr_pos[0] - goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])
def trace_nodes(curr_node:Node) -> list:
    if not curr_node:
        return []    
    traced_path = trace_nodes(curr_node.parrent) 
    traced_path.append(curr_node)
    return traced_path