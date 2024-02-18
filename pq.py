from node import Node
import typing
class pq():
    def __init__(self) -> None:
        self.l = []
        pass
    def push(self, priority: int, item: Node) -> None:
        pass

    def pop(self) -> Node:
        top:Node = self._pop()
        while not top.active:
            top = self._pop()
        return top
    def _pop(self) -> Node:
        
        pass
    def is_empty(self) -> bool:
        return bool(list) 
    def remove(self, item: Node):
        item.active = False
    def _shiftdown(self, index:int):
        pass
    def _shiftup(self, index:int):
        pass