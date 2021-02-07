class newNode: 
    def __init__(self, data):  
        self.val = data  
        self.left = self.right = None
     
# Function to print the longest path  
# of same values  
def length(node, ans): 
    if (not node):  # THIS BIT OF CODE STOPS THE RECURSION!!!
        return 0
     
    # Recursive calls to check for subtrees  
    left = length(node.left, ans)  
    right = length(node.right, ans)  
     
    # Variables to store maximum lengths  
    # in two directions  
    Leftmax = 0
    Rightmax = 0
    print(f"...cb node: {node.val}")
     
    # FIRST CB IS END OF TREE
    # If curr node and it's left child has same value  
    if (node.left and node.left.val == node.val):   
        Leftmax += left + 1  
        print(f"...cb left/LM: {node.val, Leftmax}")
       
    # If curr node and it's right child has same value  
    if (node.right and node.right.val == node.val):  
        Rightmax += right + 1
        print(f"...cb right/RM: {node.val, Rightmax}")
       
    # Here's where we increase val in array position as final answer
    # And returning maximum of two directions ensures we pass the max up the tree
    # 1st CB return 0 to prev call
    ans[0] = max(ans[0], Leftmax + Rightmax)  
    return max(Leftmax, Rightmax) 
     
# Driver function to find length of  
# longest same value path 
def pathSameValue(root): 
    ans = [0] 
    length(root, ans)  
    print(ans)
    return ans[0]
     
# Driver code  
if __name__ == '__main__': 
      
  # Let us construct a Binary Tree  
  #      2  
  #     / \  
  #    4   4  
  #   / \   \  
  #  4   9   5  
    root = None
    root = newNode(2)  
    root.left = newNode(8)  
    root.right = newNode(3)  
    root.left.left = newNode(4)  
    root.left.right = newNode(9)  
    root.right.right = newNode(5)  
    root.left.left.left = newNode(4)  
    root.left.left.left.left = newNode(4)  
    print(pathSameValue(root))
