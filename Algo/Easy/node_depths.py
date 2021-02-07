"""
The distance btw a node in a Binary Tree and the tree's root is the node's "depth".
Write function that takes BT and returns the sum of its nodes' depths/layers.
Input:
    tree =   1
           /   \
          2     3
         / \   / \
        4   5 6   7
       / \ 
      8  9 
Output:
    16

*count layers as they are traversed for each node
*total sum
*use stack? BFS? DFS?
* DFS. what is stack? put on stack, pop off from last. LIFO
*each BT node has int, L/R child
*child nodes can be BT or None
"""

def nodeDepths(tree):
    # Each node has a depth.
    # Its depth is determined by a DFS edge
    # the sum accumulates at EVERY node
    final_sum = int()
    edge_sums = []

    def inner_sum(node, final_sum):
        edge_sums.append(final_sum) # O(N)
        #print(f"...inner node/sum: {node.value, final_sum}")
        if node.left: inner_sum(node.left, final_sum+1)
        if node.right: inner_sum(node.right, final_sum+1)
        return edge_sums

    edge_sums = inner_sum(tree, 0)
    #print(sum(sums))

    return sum(edge_sums)



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None



if __name__ == "__main__":
    # Layer 1
    tree = BinaryTree(1)
    # Layer 2
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    # Layer 3
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    tree.right.left = BinaryTree(6)
    tree.right.right = BinaryTree(7)
    # Layer 4
    tree.left.left.left = BinaryTree(8)
    tree.left.left.right = BinaryTree(9)

    print(nodeDepths(tree))
