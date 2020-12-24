# Solution 1

```python
def SubarraySum (self, root: TreeNode, k: int) -> int:
    sorted_vals = []
    def inOrder(node, sorted_vaLs):
        if node:
            inOrder(node.left, sorted_vals)
            sorted_vals.append(node.val)
            inOrder(node.right, sorted_vals)

    inOrder(root, sorted_vals)

    return sorted_vals[k-1]
```

## Explanation

## Run Time

## Space Complexity

# Solution 2 DP

## Key Idea

## Explanation

## Run Time

## Space Complexity
