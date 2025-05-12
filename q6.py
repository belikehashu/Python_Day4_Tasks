class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return "Queue is empty"


q = Queue()
q.enqueue("Waheed")
q.enqueue("Muzammil")
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())
