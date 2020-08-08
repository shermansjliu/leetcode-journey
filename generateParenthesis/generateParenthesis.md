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
We use recursion to solve the problem.
- The result of backtracking is picking a subset of elements that fit within a constraint from all possibilities.
- To build up and explore each possibility, we use recursion, 
- To select an optimal element while we recuse we use a constraint
- Thus, backtracking can be broken down into three main components 
  1. Choice i.e What decision space: 
  2. Goal i.e directing recursion
  3. Constraint i.e handling base cases 

**Choice**:
- In this case, every time we recurse we choose to add an open parenthesis or a closing parenthesis to our string
**Goal**
- How we direct our recursion
- We only want to build up valid parenthesis pairings relative to n / Not recurse down invalid parenthesis combinations
- An invalid parenthesis combination is when there are more closing parenthesis that comes before opening parenthesis e.g "())" and if our string is more than > 2*n
- So we only recurse when *left* <= *right*. b/c left is # of opening parenthesis we have NOT used
**Constraint**
- Our base case is when we've exhausted all our opening and closing parenthesis i.e left == 0 and right == 0, which is when we want to add to our resulting list 
- I learned about backtracking from a video [here](https://www.youtube.com/watch?v=Zq4upTEaQyM). This legendary channel also has a video about this problem. I highly recommend checking it out since it traces through the algorithm and shows the status of the string we want to add at each recursive level

