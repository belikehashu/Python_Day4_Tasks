class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()
        return "Stack is Empty"


s = Stack()
s.push(10)
s.push(20)
print("Popped:", s.pop())
print("Popped:", s.pop())
print("Popped:", s.pop())
