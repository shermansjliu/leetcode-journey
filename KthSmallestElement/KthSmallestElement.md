```python
def kthSmallest(self, root: TreeNode, k: int) -> int:
    sorted_vals = []
    def inOrder(node, sorted_vaLs):
        if node:
            inOrder(node.left, sorted_vals)
            sorted_vals.append(node.val)
            inOrder(node.right, sorted_vals)
    
    inOrder(root, sorted_vals)

    return sorted_vals[k-1]
```

# Explanation
# An inorder traversal of a binary search tree(BST) gives us back an ordered list
# Since our sorted list is zero indexed, we take the 'k-1'th position of our sorted list