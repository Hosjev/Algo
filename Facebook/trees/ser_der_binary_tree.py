import json


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        1. run preOrder rhythm
        2. acct for all nodes with None as L/R
        """
        def _pre_order(root, data):
            if not root:
                data.append(None)
            else:
                data.append(root.val)
                data = _pre_order(root.left, data)
                data = _pre_order(root.right, data)
            return data

        # Edge Case
        if not bool(root): return json.dumps([])
        data = _pre_order(root, [])
        return json.dumps(data) # seralized string


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        1. make root from [0]
        2. reconstruct w/same preOrder rhythm
        """
        def _construct(data):
            if data[0] is None:
                data.pop(0)
                return
            root = TreeNode(data[0])
            data.pop(0)
            root.left = _construct(data)
            root.right = _construct(data)
            return root

        data = json.loads(data)
        if not bool(data): return []
        tree = _construct(data)
        return tree


def cycle(node):
    if node:
        print(node.val)
        cycle(node.left)
        cycle(node.right)

if __name__ == "__main__":
    t = TreeNode(4)
    t.left = TreeNode(-7)
    t.right = TreeNode(-3)
    t.right.left = TreeNode(-9)
    t.right.right = TreeNode(-3)
    t.right.right.left = TreeNode(-4)
    t.right.left.left = TreeNode(9)
    t.right.left.right = TreeNode(-7)
    t.right.left.left.left = TreeNode(6)
    t.right.left.left.left.left = TreeNode(0)
    t.right.left.left.left.right = TreeNode(6)
    t.right.left.left.left.left.right = TreeNode(-1)
    t.right.left.left.left.right.left = TreeNode(-4)
    t.right.left.right.left = TreeNode(-6)
    t.right.left.right.right = TreeNode(-6)
    t.right.left.right.left.left = TreeNode(5)
    t.right.left.right.right.left = TreeNode(9)
    t.right.left.right.right.left.left = TreeNode(-2)

    obj_ser = Codec()
    obj_des = Codec()
    obj_des.deserialize(obj_ser.serialize(t))
