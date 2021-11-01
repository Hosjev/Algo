class HashItem:

   def __init__(self, key, value):
       self.key = key
       self.value = value


class HashMap:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def _get_hash_idx(self, key):
        return key % self.size

    def get(self, key):
        hash_idx = self._get_hash_idx(key)
        for obj in self.hash_table[hash_idx]:
            if obj.key == key:
                return obj.value
        raise KeyError(f"Key not found: {key}")

    def set(self, key, value):
        hash_idx = self._get_hash_idx(key)
        for obj in self.hash_table[hash_idx]:
            if obj.key == key:
                obj.value = value
                return
        self.hash_table[hash_idx].append(HashItem(key, value))

    def remove(self, key):
        hash_idx = self._get_hash_idx(key)
        for idx, obj in enumerate(self.hash_table[hash_idx]):
            if obj.key == key:
                del self.hash_table[hash_idx][idx]
                return
        raise KeyError(f"Key not found: {key}")


ht = HashMap(10)
#ht.get(0)
ht.set(0, "foo")
print(ht.get(0))
print(ht.hash_table)
ht.set(10, "bar")
print(ht.get(10))
print(ht.hash_table)
ht.set(1, "baz")
ht.set(2, "far")
ht.set(3, "var")
print(ht.hash_table)
ht.remove(2)
print(ht.hash_table)
ht.remove(10)
print(ht.hash_table)
