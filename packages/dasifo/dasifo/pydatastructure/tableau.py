

class Queue():
    pass

class Stack():
    pass

class SimpleArray():
    lenght = -1
    def __init__(self, arr=[]) -> None:
        self.array = arr
        if isinstance(arr, list):
            self.lenght = len(arr)

    def append(self, elm):
        self.array.append(elm)
        self.lenght += 1
    def pop(self):
        self.array.pop()
        self.lenght -= 1
