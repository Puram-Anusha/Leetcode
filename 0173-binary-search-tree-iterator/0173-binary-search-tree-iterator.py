# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
    
        self.stack = []
        self.inorder(root)
    def inorder(self,node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        top_node = self.stack.pop()
        val = top_node.val
        if top_node.right:
            self.inorder(top_node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack)>0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()