"""
Write 3 functions that take in BST and an empty array.
Traverse the BST and its nodes' values to the input array.
The 3 functions should traverse the tree using in-order, pre-order, post-order.
In that order.
Input:
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
Output::
    tree_obj = 
            10
           /   \
          2    14
         / \   / \
        1   5 13  15
             \     \
              7     22

* follow Bst properties
* the SUCCESS of this algorithm DEPENDS on a sorted array with DISTINCT integers (no long dup lists)
answer - O(N)ST
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)


def inOrderTraverse(tree, array):
    # Return nothing but nulls and simply append as callback
    if not tree:
        return None
    inOrderTraverse(tree.left, array)
    #print(tree.value) # None answers then the 1st callback
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array # This gets returned up the stack though we have no 'state'


def preOrderTraverse(tree, array):
    # Left to right
    if not tree:
        return None
    #print(tree.value)
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array


def get_binary_base(n, x):
    if n <= 1:
        return x
    else:
        x += 1
        return get_binary_base( (n // 2), x )

def swap(a, b):
    return b, a

def minHeightBst(array):
    # This rhythm keeps finding the "middle" which is our Node
    # then sends through the next sliced array

    def add_to_tree(arr):
        if len(arr) == 1:
            tree.insert(arr[0])
            return
        elif len(arr) == 2:
            tree.insert(arr[1])
            tree.insert(arr[0])
            return
        else:
            idx_middle = len(arr) // 2
            if (len(arr) % 2) == 0:
                idx_middle -= 1
            tree.insert(arr[idx_middle])
            add_to_tree(arr[0:idx_middle])
            add_to_tree(arr[idx_middle+1:])

    
    if len(array) == 1:
        tree = BST(array[0])
    elif len(array) == 2:
        # Left side only
        tree = BST(array[1])
        tree.insert(array[0])
    else:
        root_idx = len(array) // 2
        # If we have a null root, favor left
        if len(array) % 2 == 0:
            root_idx -= 1
        tree = BST(array[root_idx])
        add_to_tree(array[0:root_idx])
        add_to_tree(array[root_idx+1:])


    return tree


if __name__ == "__main__":

    print(get_binary_base(25, 0))
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    array = [10]
    array = [4, 10]
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36]
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89, 92]
    array = [1, 2]
    array = [2]

    tree = minHeightBst(array)
    print(preOrderTraverse(tree, []))
