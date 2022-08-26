from logging.config import valid_ident
from pickletools import pylist
from . import PyList

class LinkedList(PyList):
    def __init__(self, val, next=None) -> None:
        self.val = val
        if isinstance(next, LinkedList) or next == None:
            self.next = next # must be LinkedList instance
        else:
            raise Exception("'next' must be a valid 'LinkedList' !")
        
    def add(self):
        return "LinkedList add"

    @property # because it could be changed adding, deleting nodes!
    def lenght(self):
        l = 0
        h = self
        while h.next:
            l += 1
            h = h.next
        return l

    def removeNthFromEnd(self, n:int):
        if not self.next and n==1: return None
        l = self.lenght
        if l == n-1:
            self = self.next
        h = self
        i = 0
        while h.next:
            prev = h
            if i == l-n:
                prev.next = h.next
                break
            h = h.next
            i += 1

class DoublyLinkedList(PyList):
    def __init__(self) -> None:
        pass


class CircularList(PyList):
    def __init__(self) -> None:
        pass