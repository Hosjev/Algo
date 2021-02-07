"""
Implement BFS method on the Node class, which takes in empty array and returns BFS filled.

Input:
    tree =   A
           / | \
          B  C  D
         / \   / \
        E   F G   H
           / \ \
          I   J K
Output:
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

O(v+e)T | O(v)S
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        # We need a FIFO method
        stack = []
        stack.append(self)

        return self.process_stack(stack, array)

    def process_stack(self, stack, array):
        # Add the OBJECT to the stack
        while stack:
            node = stack.pop(0)
            array.append(node.name)
            for child in node.children:
                stack.append(child)

        return array


if __name__ == "__main__":
    # Layer 1
    # Now A has an array attribute called children
    tree = Node("A")
    tree.addChild("B") # 0
    tree.addChild("C") # 1
    tree.addChild("D") # 2
    #tree.children[0] # B
    tree.children[0].addChild("E") # 0
    tree.children[0].addChild("F") # 1
    #tree.children[2] # D
    tree.children[2].addChild("G") # 0
    tree.children[2].addChild("H") # 1
    #tree.children[0][1] # F
    tree.children[0].children[1].addChild("I") # 1
    tree.children[0].children[1].addChild("J") # 1
    #tree.children[2][0] # G
    tree.children[2].children[0].addChild("K") # 0


    print(tree.breadthFirstSearch([]))
