from __future__ import annotations
import random
class Node:
    def __init__(self, x:int, y:int, g_val:int, h_val:int, parrent:Node) -> None:
        self.x = x
        self.y = y
        self.g_val = g_val
        self.h_val = h_val
        self.f_val = g_val + h_val
        self.parrent = parrent
    def __repr__(self) -> str:
        s = ""
        if not self: 
            return
        if self.parrent:
            s = "(%d, %d) P: (%d, %d)" % (self.x, self.y, self.parrent.x, self.parrent.y)
        else:
            s = "(%d, %d) P: None" % (self.x, self.y)
        return s
    def __lt__(self, other:Node) -> bool:
        # favors larger g_vals. so explores more towards the goal state
        return self.g_val > other.g_val
    def __eq__(self, other:Node) -> bool:
        return self.x == other.x and self.y == other.y