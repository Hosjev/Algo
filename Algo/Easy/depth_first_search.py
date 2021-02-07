"""
Given a node class that has a name and an array of optional children. When put together, they
form acyclic tree-like structure. Implement DFS method on node class which takes an empty array,
traverses the tree using DFS (specifically navigating left to right) then store all names of
nodes and return them.
Input:
    graph =   A0
           /  |  \
          B0 C1  D2
         /  \    / \
        E0   F1 G0  H1
            / \  \
          I0  J1 K0
Output:
    ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]]
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        #return self
        # the return seems superfluous

    def depthFirstSearch(self, array):
        # Write your code here.
        # 1st obj written to array is self "A"
        # This method takes ITSELF and the array
        array.append(self.name)
        for child in self.children: # O(v+e)
            child.depthFirstSearch(array)
            # This notation is VERY important.
            # The method reads self, and we indicate it
            #  with the OBJ.method. But you can pass anything
            #  to method with SELF.

        return array


if __name__ == "__main__":
    tree = Node("A")
    tree.addChild("B")
    tree.children[0].addChild("E")
    tree.children[0].addChild("F")
    tree.children[0].children[1].addChild("I")
    tree.children[0].children[1].addChild("J")
    tree.addChild("C")
    tree.addChild("D")
    tree.children[2].addChild("G")
    tree.children[2].children[0].addChild("K")
    tree.children[2].addChild("H")


    print(tree.depthFirstSearch([]))
