# Library for functions related to graphing, building, and parsing trees
import queue
import sys
from collections import deque


class TypeFlagGraphError(Exception):
    pass


class Graph:
    """Graph object builder

    Input:
        num_nodes (int): number of vertices/nodes in graph.
        start (int or str): place to begin DFS/BFS/etc. (default 0)
        reverse (bool): adds reverse source to destination (for undirected graphs/defaults to True).
            *add_edge method ex: obj.add_edge(0, 1)
            *directed(weight/outbound): obj.add_edge(0, 1, 5)
            *directed edges w/o weights: obj.add_edge(0, 1) (call obj.addInOutEdges)
            *reference obj.graph.items() to preserve node names

    Returns:
        Graph object of nodes with children as nested lists.
        Nothing but adjacency list iterators.
        .adjList as non-OOP lists per node
        .adjacent list as objects lists
        In/outbound edges can be tracked with .addInOutEdges() method.
         *obj.inEdges & obj.outEdges arrays
    """

    def __init__(self, num_nodes, start = 0, reverse = True):
        self.num_nodes = num_nodes
        self.adjacent = [ [] for x in range(self.num_nodes) ]
        self.parent = None
        self.id = start
        # The default (undirected) is to add a vertice pairing for both (0-1, 1-0)
        self.reverse = reverse

    def add_edge(self, src, dest, weight = None):
        # Add from and to as objects to node adjacency list
        # This tuple execution needs to go away and be replaced w/attr
        #  *directed == no reverse and *dir_weight == directed/weighted
        to_node = Node(dest, src, weight)
        self.adjacent[src].append(to_node)
        if self.reverse == True:
            from_node = Node(src, dest, weight)
            self.adjacent[dest].append(from_node)

    def add_in_out_edges(self):
        # Tack easy-to-iterate lists onto main object
        self.outEdges = [0] * self.num_nodes
        self.inEdges = [0] * self.num_nodes
        for node in range(self.num_nodes):
            for child in self.adjacent[node]:
                self.outEdges[node] += 1
                self.inEdges[child.eTo] += 1

    def add_net_edge(self, eFrom, eTo, capacity):
        # Method for adding Fulkerson-type edges (network flow)
        if capacity <= 0: raise IllegalArgumentException("Capacity must be > 0")
        forward = Node(eTo, eFrom, capacity = capacity)
        backward = Node(eFrom, eTo, capacity = 0)
        forward.residual = backward
        backward.residual = forward
        self.adjacent[eFrom].append(forward)
        self.adjacent[eTo].append(backward)

    def twoD_matrix(self):
        # Return a classic adjacency list n[0][1]
        pass

    def preserve_keys(self, graph):
        # Method sets a simple array for integer based tree nodes
        self.graph = graph

    def set_undirected_list(self):
        self.adjList = [[] for x in range(self.num_nodes)]
        for node, vals in self.graph.items():
            self.adjList[node] = vals



class Node:
    def __init__(self, child, parent, weight = None, capacity = None):
        # Graph and flow attributes
        self.id = self.eTo = child
        self.parent = self.eFrom = parent
        self.left = self.right = None
        self.weight = weight
        # Network flow attributes
        self.capacity = capacity
        self.flow = 0
        self.residual = None

    def is_residual(self):
        # Boolean
        return self.capacity == 0

    def remaining_capacity(self):
        # Integer
        return self.capacity - self.flow

    def augment(self, bottleNeck):
        self.flow += bottleNeck
        # below is done thru helper method
        residual.flow -= bottleNeck


class TreeNode:
    """Tree object builder (intended for nesting)

    Input:
        Graph (str or int): a starting node/root for tree.
        Children (): usually an empty list.

    Returns:
        Nothing.
    """

    def __init__(self, val, children):
        self.id = val
        self.parent = val # future use
        self.children = children
        self.left = self.right = None

    def add_children(self, nodes):
        [self.children.append(node) for node in nodes]


class GraphQueue:
    """Class for building various graph/search queues.

    Input:
        QueueType (str): types accepted [fifo, lifo, pq, deque]
        QueueSize (int): defaults to zero (infinite).

    Returns:
        buildQ method returns the queue itself.

    """
    def __init__(self, qtype, qsize = 100):
        self.qsize = qsize
        if qtype == "fifo":
            self.qtype = queue.Queue(self.qsize)
        if qtype == "lifo":
            self.qtype = queue.LifoQueue(self.qsize)
        if qtype == "pq":
            self.qtype = queue.PriorityQueue(self.qsize)
        if qtype == "deque":
            self.qtype = deque()
    def buildQ(self):
        try:
            return self.qtype
        except:
            print(f"Could not build queue for {self.qtype}:",
                    sys.exc_info()[0])


def root_tree(g, rootID = 0):
    """Rooting a tree function

    Input:
        Graph (object): contains graph/matrix/adjacency list.
        rootID (str or int): root node for tree.

    Returns:
        The buildTree method after run (nested tree objects).
    """
    root = TreeNode(rootID, [])
    return build_tree(g, root, None)


def build_tree(g, node, parent = None):
    """Building a tree from matrix/adjacency list.

    Input:
        Graph (object): contains graph/matrix/adjacency list.
        Node (object): parent or child tree node.
        Parent (object): parent of 'node' (default: none).

    Returns:
        Nested collection of nodes (rooted tree).
    """
    # DFS dive that builds tree of objects
    for child in g.adjList[node.id]:
        if (parent != None and child == parent.id):
            continue # this stops us from going UP the tree
        childObj = TreeNode(child, [])
        node.children.append(childObj)
        build_tree(g, childObj, node)
    return node 


def find_center(g):
    """Find the center of a tree by evaluating edges.

    Input:
        Graph (object/dict): tree mapped in node->to->children.
        ---> current library Graph class.

    Returns:
        Evaluate tree from edges to center then return
        a list containing one or more centers of a tree.

    """
    # Setup variables to use during iterations
    n = len(g.adjList)
    degree = [0 for x in range(n)]
    edge_leafs = []

    # Process beginning edge leafs in graph
    for i in range(n):
        degree[i] = len(g.adjList[i])
        if degree[i] <= 1:
            edge_leafs.append(i)
            degree[i] = 0
    processed = len(edge_leafs) # contains leafs only

    # While leaves is less than total number of nodes
    while processed < n:
        new_leaves = []
        for leaf in edge_leafs:
            for neighbor in g.adjList[leaf]:
                degree[neighbor] = degree[neighbor] - 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
            degree[leaf] = 0
        # Increase total count of processed edges and do it again
        processed += len(new_leaves)
        edge_leafs = new_leaves

    return edge_leafs


def encode(node):
    """Encode a tree into string.

    Input:
        Node (object): as from current TreeNode class
           with 'children' attribute.

    Returns:
        String of empty tuples.
        Ex-  ((((()))())(()))
    """
    # Recursion to return encoding string
    if node == None:
        return ""
    labels = []
    for child in node.children:
        labels.append(encode(child))
    labels.sort()
    result = ""
    for label in labels:
        result += label
    return "(" + result + ")"


def trees_isomorphic(g1, g2):
    """Isomorphic match is made from input of graphs.

    Input:
        1 and 2 Graph (Graph object): contains child list.
        Classes, methods,and functions referenced locally.

    Returns:
        Boolean: True if graph 1 and 2 are structurally same.
    """
    tree1_centers = find_center(g1)
    tree2_centers = find_center(g2)
    tree1_rooted = root_tree(g1, tree1_centers[0])
    tree1_encoded = encode(tree1_rooted)
    for center in tree2_centers:
        tree2_rooted = root_tree(g2, center)
        tree2_encoded = encode(tree2_rooted)
        if tree1_encoded == tree2_encoded:
            return True
        return False


def cascade(parent):
    """Print to screen function of id's inside nested Tree.

    Input:
        Tree (object): made from TreeNode.
        Recursive method.

    Returns:
        Print to screen/output device.
    """
    for child in parent.children:
        print(f"Parent {parent.id} child {child.id}")
        print(f"-->child L {parent.left} - R {parent.right}")
        cascade(child)


def add_binary_positions(parent):
    """Creates left and right positions for BINARY tree dive.

    Input:
        Graph/Tree (object): created from TreeNode and buildTree.

    Returns:
        Returns the same object (left and right node attributes).
    """
    parent.left = parent.children[0]
    parent.right = parent.children[1]
    def subtree(parent):
        for child in parent.children:
            if len(child.children) == 1:
                child.left = child.children[0]
            if len(child.children) == 2:
                child.left = child.children[0]
                child.right = child.children[1]
            subtree(child)
        return parent
    return subtree(parent)
    

def calc_tree_height(node):
    """Calculate tree height and return longest edge path.
    Input node (object) created with TreeNode."""
    if node == None:
        return -1
    # node.left and right below are whole objects
    return max(calc_tree_height(node.left),
               calc_tree_height(node.right)) + 1


def top_sort(g):
    # We ultimately return the order list
    # *variable "i" superfluous but dfs_top recursion needs it
    visited = [False] * g.num_nodes
    order = [0] * g.num_nodes
    i = g.num_nodes - 1

    for node in range(g.num_nodes):
        if not visited[node]:
            i = dfs_top(i, node, visited, order, g)

    return order


def dfs_top(i, node, visited, order, g):
    visited[node] = True

    for edge in g.adjacent[node]: # edge is a tuple
        if not visited[edge.eTo]:
            i = dfs_top(i, edge.eTo, visited, order, g)

    order[i] = node
    return i - 1
