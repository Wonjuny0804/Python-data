"""
Queue
data in and out FIFO
First In First Out

functions of queue
- enqueue : like a push in stack
- dequeue : like a pop in stack
- peek/front : see the one in the front
- empty : check if the queue is empty
- size : returns the size of the queue

"""

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty.")

    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    queue = Queue()
    print("Is the queue empty? {0}".format(queue.isEmpty()))
    print("Adding numbers 0~9 to the queue.")
    for i in range(10):
        queue.enqueue(i)

    print("Queue size : {0}".format(queue.size()))
    print("Peek : {0}".format(queue.peek()))
    print("dequeue : {0}".format(queue.dequeue()))
    print("Peek : {0}".format(queue.peek()))
    print("Is the queue empty? {0}".format(queue.isEmpty()))

    print(queue)