# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        1. run BFS w/q
        2. acct for all nodes with 'None' as L/R
        """
        from queue import Queue
        import json
        q = Queue()
        data = list()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node:
                data.append(node.val)
                q.put(node.left)
                q.put(node.right)
            else:
                data.append("None")
        return json.dumps(data) # seralized string


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        1. make root from [0]
        2. reconstruct tree from (i * 2) + 1/2
        """
        def _construct(index, data):
            node = TreeNode(data[index])
            left = (index * 2) + 1
            right = (index * 2) + 2
            if data[left] is not None:
                node.left = TreeNode(data[left])
                _construct(left, data)
            if data[right] is not None:
                node.right = TreeNode(data[right])
                _construct(right, data)
            return

        import json
        data = json.loads(data)
        tree = TreeNode(data[0])
        _construct(1, data)
        _construct(2, data)
        return tree

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
