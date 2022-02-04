class Node:

    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BST:

    def recurse(self, parent, subLeft, subRight):
        if not subLeft and not subRight:
            return
        if subLeft:
            m_l = len(subLeft) // 2
            parent.left = Node(subLeft[m_l])
            self.recurse(parent.left, subLeft[0:m_l], subLeft[m_l+1:])
        if subRight:
            m_r = len(subRight) // 2
            parent.right = Node(subRight[m_r])
            self.recurse(parent.right, subRight[0:m_r], subRight[m_r+1:])
        
    def make_tree(self, array):
        middle = len(array) // 2
        tree = Node(array[middle])
        self.recurse(tree, array[0:middle], array[middle+1:len(array)])
        return tree

    def cycle(self, node):
        if not node:
            return
        self.cycle(node.left)
        print(node.value)
        self.cycle(node.right)


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    tree = BST().make_tree(a)
    BST().cycle(tree)


#main()
