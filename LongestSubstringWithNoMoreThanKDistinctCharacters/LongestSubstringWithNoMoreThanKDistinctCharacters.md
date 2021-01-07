# Solution Sliding Window

```python
def getLengthofLongestSubstring(k, s):
    start = 0
    end =  0
    res = 0
    characters = {}
    while end < len(s):
        characters[s[end]] = characters.get(s[end], 0) + 1
        if len(characters.keys()) > k:
            while len(characters.keys()) > k:
                characters[s[start]] -= 1
                if characters[s[start]] == 0:
                    del characters[s[start]]
                    start += 1
        res = max(res, start-end + 1)
        end += 1

    return res
```

## Explanation

## Run Time

## Space Complexity
