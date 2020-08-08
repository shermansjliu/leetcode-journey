# Solution 1 Verbose 
```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    min_word = min(strs, key=len) #O(n)
    prefix = ""
    for i in range(len(min_word)): #O(1)
        matches = True
        for word in strs:
            if min_word[i] != word[i]:
                matches = False
                break
        if matches:
            prefix += min_word[i]
        else:
            break
    return prefix


```


### Explanation

# Solution 2 - same big-O but faster run time

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    if strs == [""]:
        return ""
    
    min_word = min(strs, key=len) #O(n)
    prefix = ""
    for i in range(len(min_word)): #O(1)
        for word in strs:
            if min_word[i] != word[i]:
                return min_word[:i]
    return min_word
```
### Explantion