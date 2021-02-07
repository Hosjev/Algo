"""
You're given 3 inputs, all of which are instances of an AncestralTree class that has
properties pointing to their youngest ancestor. The 1st input is the top ancestor in an
ancestral tree (ie-the only instance that has no ancestor--its ancestor property
points to None. The other 2 inputs are descendants in the ancestral tree.
Write a function that returns the youngest common ancestor to the 2 descendants.
Note that a descendant is considered its own ancestor. So in the simple ancestral tree
below, the youngest common ancestor to nodes A and B is node A.

Input:
    tree = A
          /
         B
Input:
    tree =   A
           /   \
          B     C
         / \   / \
        D   E F   G
       / \
      H   I
    topAncestor = node A
    descendantOne = node E
    descendantTwo = node I

Output:
    Node B

O(d)T - depth | O(1)S
"""

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    # Get depths and equalize them
    depth_one = get_depth_of_member(topAncestor, descendantOne)
    depth_two = get_depth_of_member(topAncestor, descendantTwo)

    print(depth_one, depth_two)
    # If conditions to meet the two cases
    if depth_one > depth_two:
        descendantOne = equalize(descendantOne, (depth_one - depth_two))
    else:
        descendantTwo = equalize(descendantTwo, (depth_two - depth_one))

    # Traveling UP along the tree until a match is made
    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne # Just pick one


def equalize(descendant, difference):
    # Need to reach the same level
    while difference != 0:
        descendant = descendant.ancestor
        difference -= 1
    return descendant


def get_depth_of_member(elder, descendant):
    depth = 0
    while descendant != elder:
        descendant =  descendant.ancestor
        depth += 1
    return depth



if __name__ == "__main__":
    # Layer 1
    a = AncestralTree("A")
    # Layer 2
    b = AncestralTree("B")
    b.ancestor = a
    c = AncestralTree("C")
    c.ancestor = a
    # Layer 3
    d = AncestralTree("D")
    d.ancestor = b
    e = AncestralTree("E")
    e.ancestor = b
    f = AncestralTree("F")
    f.ancestor = c
    g = AncestralTree("G")
    g.ancestor = c
    # Layer 4
    h = AncestralTree("H")
    h.ancestor = d
    i = AncestralTree("I")
    i.ancestor = d


    node = getYoungestCommonAncestor(a, e, i)
    print(node.name)
    node = getYoungestCommonAncestor(a, b, h)
    print(node.name)
