from Node import Node


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top == None

    def peek(self):
        if self.isEmpty():
            return
        return self.top

    def push(self, data):
        if data is None:
            return
        node = Node(data)
        if self.isEmpty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1
        return self.peek()

    def pop(self):
        if self.isEmpty():
            return
        else:
            popped = self.top
            self.top = self.top.next
            popped.next = None
            self.size -= 1
            return popped

    def Size(self):
        return self.size
