import sys
sys.path.append("./Facebook")
from bst_min_height import BST

class NodeSearch:

    def sec_largest(self, tree):
        array = self.cycle(tree, [])
        if len(array) == 0: raise TypeError
        if len(array) == 1: raise ValueError
        return sorted(array)[-2]

    def cycle(self, node, arr):
        if not node:
            return
        self.cycle(node.left, arr)
        arr.append(node.value)
        self.cycle(node.right, arr)
        return arr


def main():
    a = [1,2,3,4,5,6,7,8]
    a = [1]
    tree = BST().make_tree(a)
    print(NodeSearch().sec_largest(tree))


main()
