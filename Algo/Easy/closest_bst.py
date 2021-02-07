"""
Write function that takes in Binary Search Tree and target int value and returns closest value
in the target value contained in BST.
Input:
    tree =   10
           /    \
          5     15
         /  \  /  \
        2   5 13  22
       /       \
      1        14
    target = 12
Output:
    13

*assume only one closest value
*each BST node has an int value, a L and R child.
*any BST node is a valid node if ONLY if it satisfies BST property:
    its value is greater than any node to its L;
    its value is less than or equal to the values of every node to its R;
    its children nodes are also valid nodes or None
*what would be the recursive method? a function that took the node as input instead of stack
*recursive generally cleaner code?
*with this method its obvious where the tree might fail a BST test
*recursion TC increases, iterative Sc increases
"""

def findClosestValueInBst(tree, target):
    # Traverse tree checking only nodes that pass the BST test
    node_negation = ( tree.value, abs(target - tree.value))

    def is_valid_bst(n, l, r): # O(1)
        b = True
        if l: b = n.value > l.value
        if r: b = n.value <= r.value
        return b

    def eval_node(val, nn):
        if abs(target - val) < nn[1]:
            nn = (val, abs(target - val))
        return nn

    stack = [ (tree, tree.left, tree.right) ] # O(N)
    while stack:
        node, left, right = stack.pop()
        if is_valid_bst(node, left, right):
           if left:
               node_negation = eval_node(left.value, node_negation)
               stack.append( (left, left.left, left.right) )
           if right:
               node_negation = eval_node(right.value, node_negation)
               stack.append( (right, right.left, right.right) )
        else:
            return None

    return node_negation[0]


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    # Layer 1
    tree = BST(10)
    # Layer 2
    tree.left = BST(5)
    tree.right = BST(15)
    # Layer 3
    tree.left.left = BST(2)
    tree.left.right = BST(5)
    tree.right.left = BST(13)
    tree.right.right = BST(22)
    # Layer 4
    tree.left.left.left = BST(1)
    tree.right.left.right = BST(14)

    t = 12
    print(findClosestValueInBst(tree, t))
