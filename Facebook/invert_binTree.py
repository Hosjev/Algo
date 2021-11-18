class Node:

    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class InvertBinaryTree:
    """ O(N) """
    def eval(self, tree):
        # As we approach level 2, do WHOLE subtree
        if not tree:
            return
        self.eval(tree.left)
        self.eval(tree.right)
        tree.left, tree.right = tree.right, tree.left
        return tree


def main():
    tree = Node(5)
    tree.left = Node(2)
    tree.right = Node(7)
    tree.left.left = Node(1)
    tree.left.right = Node(3)
    tree.right.left = Node(6)
    tree.right.right = Node(9)

    i_tree = InvertBinaryTree().eval(tree)
    print(i_tree.left.value, i_tree.right.value)

main()
