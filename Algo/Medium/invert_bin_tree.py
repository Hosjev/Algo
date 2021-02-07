"""
Write a function that takes in Binary Tree and inverts it. Swap every left node for its
corresponding right node.
Input:
    tree_obj = 
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
       / \           
      8   9           
Output:
             1
           /   \
          3     2
         / \   / \
        7   6 5   4
                 / \ 
                9   8 

* follow Bst properties
answer - O(N)T O(d)S --N=nodes, d=depth
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def swap(a, b):
    return b, a


def invertBinaryTree(tree):
    # Iterative
    # Using a BFS method with stack
    # How you made this awful and confusing was thinking you
    #  you needed to traverse the tree. You do NOT. Each thing
    #  stored at L and R is an object w/a value that can be changed.
    # Also, I dismissed this first thought b/c I thought it was cheating.
    #   To change the values in place. WHY? It seemed too easy. :(
    stack = [tree]

    while stack:
        node = stack.pop(0) # FIFO
        # To add nulls to stack
        if node:
            node.left, node.right = swap(node.left, node.right)
            stack.append(node.left)
            stack.append(node.right)

    return tree


def invertBinaryTree(tree):
    if not tree:
        return None

    # Process each left right, even None's
    tree.left, tree.right = swap(tree.left, tree.right)
    
    # Run the process, left to right for every node
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

    # Return tree up the stack
    return tree


def preOrderTraverse(tree, array):
    # Left to right
    if not tree:
        return None
    #print(tree.value)
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    # [1, 2, 6, 5, 22, 15, 10]
    # bottom up
    if not tree:
        return None
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    #print(tree.value)
    array.append(tree.value)
    return array


def experiment(tree, array):
    if not tree:
        return None
    experiment(tree.left, array)
    experiment(tree.right, array)
    array.append(tree.value)
    return array



if __name__ == "__main__":

    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    tree.right.left = BinaryTree(6)
    tree.right.right = BinaryTree(7)
    tree.left.left.left = BinaryTree(8)
    tree.left.left.right = BinaryTree(9)


    print(postOrderTraverse(tree, []))
    print(invertBinaryTree(tree))
    print(postOrderTraverse(tree, []))
