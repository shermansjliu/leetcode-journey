# Solution

```python
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: 
    if not q and not p:
        return True

    if p and not q or q and not p:
        return False
    if p.val !=  q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## Key Ideas
- For those who know DFS. This is just [DFS_visit](https://www.youtube.com/watch?v=AfSk24UTFS8) on left and right branch while checking equality of elements 
- Compare the roots of *p* and *q*, recursively compare *q*'s left subtree to *p*'s left subtree and *q*'s right subtree to *p*'s right subtree and 


