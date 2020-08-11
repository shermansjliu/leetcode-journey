# Solution 
```python
def permute(self, nums: List[int]) -> List[List[int]]:
    curr = []
    result = []
    def backtrack_dfs(result, curr, nums):
        if len(nums) == 0:
            result.append(curr)
        for i in range(len(nums)):
            backtrack_dfs(result, curr + [nums[i]] ,nums[:i] + nums[i+1:])
    backtrack_dfs(result, curr, nums)
    return result
```
# Explannation
- The problem can be represented using a tree
- At the bottom of the tree lies each permutation, so we use DFS to reach the bottom and append it to our list
- At each level, we decrease the number of letters we can use. i.e we decrease our input space
**Pseudocode**
- Create a new list to store our result and our potential permutation 
- In our recursive function
- Base case: when our input_space is 0, we've exhausted all letters so we can add our current potential permutation to our result
- For every character in our current input space
  - We make a recursive call
  - The recursive call, adds a letter to our potential permutation `curr + [nums[i]]` and shrinks our input space by removing the letter we just used `nums[:i] + nums[i+1:]`

This problem is best explained with a visual tracing of the problem. I highly recommend checking out BackToBackSwe's explanation on Youtube. Leetcode's discussion board helped, but BackToBackSwe's video really solidified my understanding and approach.

