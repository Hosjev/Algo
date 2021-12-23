class BST:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class DLL:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next



def in_order_traverse(tree, ordered_array):
    if tree is None:
        return None

    in_order_traverse(tree.left, ordered_array)
    ordered_array.append(tree.value)
    in_order_traverse(tree.right, ordered_array)

    return ordered_array



if __name__ ==  "__main__":
    # Build tree
    tree = BST(100)
    tree.left = BST(50)
    tree.right = BST(200)
    tree.left.left = BST(25)
    tree.left.right = BST(75)
    tree.left.left.right = BST(30)
    tree.left.right.left = BST(60)
    tree.right.left = BST(125)
    tree.right.right = BST(350)


    order_arr = in_order_traverse(tree, [])
    print(order_arr)

    previous = None
    for i in range(len(order_arr) - 1):
        current = DLL(order_arr[i]) # 25 30
        next = DLL(order_arr[i+1]) # 30 50
        current.next = next
        current.prev = previous # None
        previous = current # 25 30

    print(current.value)
