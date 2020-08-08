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
**Pseudocode**
- if the string is empty return an empty string
- find the word with the lowest length : The length of the longest prefix is upperbounded by the length of the shortest word
- For each character *c* in the shortest word
    - Check that the corresponding character in every other word
    - if there is a mismatch change our *matches* boolean to False and stop the loop
- if *matches* is True, add *c* to our *prefix*  
- if *matches* is False, we have our longest prefix, thus we break the entire loop
- return *prefix*


# Solution 2 - same run time, but more elegant solution

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