class FifoQueue:

    def __init__(self):
        self.enQ = list()
        self.deQ = list()

    def _eval_stacks(self, source, dest):
        while source:
            dest.append(source.pop())

    def enqueue(self, item):
        self._eval_stacks(self.deQ, self.enQ)
        self.enQ.append(item)

    def dequeue(self):
        self._eval_stacks(self.enQ, self.deQ)
        return None if not bool(self.deQ) else self.deQ.pop()



def main():
    q = FifoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.enQ)
    print(q.dequeue())
    print(q.enQ)
    q.enqueue(5)
    q.enqueue(6)
    print(q.enQ)
    print(q.dequeue())
    print(q.enQ)

main()
