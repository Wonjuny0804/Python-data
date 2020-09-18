class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print("Queue is empty!")

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("Queue is empty!")

    def isEmpty(self):
        return not bool(self.in_stack) or bool(self.out_stack)

if __name__ == "__main__":
    queue = Queue()
    for i in range(20):
        queue.enqueue(i)

    print(queue)
    print("dequeue : {}".format(queue.dequeue()))
    print("size : {}".format(queue.size()))

    print(queue)