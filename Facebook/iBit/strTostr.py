class Node:
    """ Potential solution for using index references """
    def __init__(self, value, indices):
        self.value = value
        self.indices = []

class Trie:
    def __init__(self, string):
        self.root = {}
        self.symbol = "*"
        self.build_root(string)

    def build_root(self, string):
        for i in range(len(string)):
            self.build_suffix(i, string)
        return self.root

    def build_suffix(self, i, string):
        current_node = self.root
        for suff in range(i, len(string)):
            char = string[suff]
            if not char in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node[self.symbol] = True

    def search(self, pattern):
        node = self.root
        idx_flag = None
        for char in pattern:
            if char in node:
                node = node[char]
            else:
                return False
        return True


class Solution:
    """ Returns bool """
    def StrStr(self, a, b):
        # Edge Case(s)
        if len(a) == 0 or len(b) == 0:
            return False

        trie = Trie(a)
        return trie.search(b)


a = "hello"
b = "heo"
print(Solution().StrStr(a, b))
