import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, prioirty):
        heapq.heappush(self._queue,(-prioirty, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "Item({0!r})".format(self.name)

def test_priority_queue():
    '''push and pop are all O(logN).'''

    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test2'), 4)
    q.push(Item('test3'), 3)
    assert(str(q.pop()) == "Item('test2')")
    print("Testified!")

if __name__ == "__main__":
    test_priority_queue()