# Solution DFS with STack

## Key Insight

- Store additional information in the stack. In this case store the list of values of nodes visited so far (including the one visited) i.e path

```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def PathSumII(root:TreeNode, s:int ):
    if root is None:
        return []
    res = []
    stack = [] #Create a stack for dfs traversal
    stack.append((root, [root.val])) #Add the root node to the stack
    while len(stack) > 0:

        node, visited = stack.pop()
        if node.left is None and node.right is None: #If this node is a leaf, i.e has no children we check if its sum of the path is == s and add it to our result
            if sum(visited) == s:
                res.append(visited)
        if node.left:
            stack.append((node.left, visited + [node.left.val]))
        if node.right:
            stack.append((node.right, visited + [node.right.val]))

    return res
```

## Run Time

- N nodes, visit each node at most once O(N)

## Space Complexity

- Worst case is if we need to store every single node i.e all paths from root to children sum up to s
- N nodes, O(N)
