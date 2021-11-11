import unittest


class PQNode:

    def __init__(self, key, obj):
        self.key = key
        self.obj = obj

class PriorityQueue:
    """ objects stored as tuples """
    def __init__(self):
        self.array = []

    def insert(self, node):
        self.array.append(node)
        return self.array[-1]

    def extract_min(self):
        if not self.array: return
        q_minimum = float("+inf") # pointer
        for idx, item in enumerate(self.array):
            if item.key < q_minimum:
                q_minimum = item.key
                target = idx
        return self.array.pop(target)

    def decrease_key(self, new_key, obj):
        if not self.array: return
        for item in self.array:
            if item.obj == obj:
                # missing less than check/decr
                item.key = new_key
                return item
        return f"Obj {obj} not found"


class TestPQ(unittest.TestCase):

    def test_empty(self):
        pq = PriorityQueue()
        self.assertEqual(pq.extract_min(), None)

    def test_objects(self):
        pq = PriorityQueue()
        obj = pq.insert(PQNode(0, "a"))
        self.assertIsInstance(obj, object)

    def test_failed_key(self):
        pq = PriorityQueue()
        pq.insert(PQNode(0, "a"))
        ans = pq.decrease_key(1, "b")
        self.assertIsInstance(ans, str)


if __name__ == "__main__":
    unittest.main()
