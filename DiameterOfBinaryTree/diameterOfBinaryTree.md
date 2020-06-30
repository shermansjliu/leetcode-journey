
# Solution #1. More intuitive, less efficient
```python
  def diameterOfBinaryTree(self, root: TreeNode) -> int:
      if root is None or root == []:
          return 0
      l_diameter = self.diameterOfBinaryTree(root.left)
      r_diameter = self.diameterOfBinaryTree(root.right)
      
      l_height = self.height(root.left)
      r_height = self.height(root.right)
      
      return max(l_height + r_height, l_diameter, r_diameter)
  
  def height(self, root: TreeNode) -> int:
      if root is None:
          return 0
      return max(self.height(root.left), self.height(root.right))+1
```

## Explanation
If a binary tree is empty or null return 0
If a binary tree has children, the maximum diameter (a.k.a longest path) is one of three options
1. The diamter of the right subtree (Figure A)
2. The diamter of the left subtree (Figure B)
3. The longest path is a path through both subtrees and the parent node, which is the height of the left subtree + the height of the right subtree

Our answer is the maximum of these three components 


# Solution #2 (More efficeint) (IPR)

## Explanation













