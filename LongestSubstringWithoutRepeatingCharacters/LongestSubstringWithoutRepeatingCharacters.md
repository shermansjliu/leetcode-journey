# Solution # 1 (Brute Force)
```python
def lengthOfLongestSubstring(self, s: str) -> int:
  res = 0
  for i in range(len(s)):
    
    curr_set = set()
    for j in range(i+1, len(s)):
      if s[j] not in curr_set:
        curr_set.add(s[j])
        res = max(len(curr_set), res)
      else:
        break

return res
  
```
### Explanation
- Look at the length of all substrings with distinct characters and find the global length

## Running time and Space time
n = len(s)
Run time: O(n^2)
m = number of unique characters
Space time: O(m)

# Solution # 2 (Sliding Window)
```python
def lengthOfLongestSubstring(self, s: str) -> int:
  left = 0
  right = 0
  curr_set = {}
  res = 0 
  while right < len(s):
    if s[right] not in curr_set:
      curr_set.add(s[right])
      right += 1
      res = max(len(curr_set), res)
    else:
      curr_set.remove(s[l])
      left += 1
   return res
  
```

### Explanation
- Sliding window approach. Two pointers, left and right, which represent the two ends of our window
- When we come across a character not in our window, we continue to expand our window and update res
- When we come across a duplicate, we increment left and shirnk our window
- Why does this work?
  - case 1: Coming across a non-duplicate character, aka our subtring can be longer so we duplicate
  - case 2: Comming across a duplicate character, let's denote it as c for now *c*
    - The new unique substring to test would start from anywhere beween `[l+1:r+1]` so we shrink the window until we only have distinct characters in it


## Running time and Space time
n is len(s)
m is # of unique characters in s
- Running Time O(n) 
- Space time O(m)