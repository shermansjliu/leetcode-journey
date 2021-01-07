# Sliding Window

## Key Insight

- For a sliding window solution we need to identify 2 things

1. window's data: What do we want to collect from the window
2. Condition
   1. Condition to expand the window
   2. Condition to shirnk the window

**Windows Data**

- Based on our output we want to know the size of the window: r - l + 1
- We also want to collect the highest character frequency in the window
  - Why?
  - Consider 'AAABCDA', k = 2
    ^ ^
  - For a window with a valid string, the # characters that should be flipped are be all the other characters in the window that are NOT the character of the highest freq
  - For AAABC, it's clear that the max string with character replacement is obtained by keeping A and flipping B,C

**Condition to keep the window valid**

- Expand: Keep expanding the end of the window as long as the # flipped chars < k:
  - #Characters in the window r - l + 1
  - #Characters we don't want to flip = _highest_freq_in_window_
  - Flipped characters = r - l + 1- highest_freq_in_window < k
- Shrink: Increase the start of the window until # flipped chars < k:

```python

 def characterReplacement(self, s: str, k: int) -> int:
    highest_freq_in_window = 0
    l = 0
    dct = {}
    res = 0
    for r in range(len(s)):
        dct[s[r]] = dct[s[r]].get(0, s[r]) + 1
        highest_freq_in_window = max(highest_freq_in_window, dct[s[r]])
        while r - l + 1 - highest_freq_in_window < k:
            #Why don't we need to update highest_freq_in_window\
            #Our answer is upperbounded by s upperbounded by highest_freq_in_window + k.
            #Since this is a maximation problem we care when highest_freq_in_window increases.

            dct[s[r]] -= 1
            l += 1
        res = max(res, r - l + 1)
```
