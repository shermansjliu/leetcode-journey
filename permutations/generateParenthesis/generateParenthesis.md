Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```
# Solution
```python
def generateParenthesis(n:int)->List[str]:
  left = n
  right = n
  result = []
  curr = ""
  def generate(left, right, result, curr):
    if left == 0 and right == 0:
      result.append(curr)
    else:
      if left <= right:
        if left > 0:
          generate(left-1, right, result, curr + "(")
        if right > 0:
          generate(left, right-1, result, curr + ")")
  generate(left, right, result, curr)
  return result
```


### Explanation
