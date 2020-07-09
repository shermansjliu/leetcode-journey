# Solution #1

```python
def removeDuplicates(self, nums: List[int]) -> None:
    if len(nums) == 0 or is None:
        return 0
    last_non_duplicate = 0
    for i in range(1, len(nums)):
        if nums[last_non_duplicate] != nums[i]
        last_non_duplicate += 1
        nums[last_non_duplicate], nums[i] = nums[i], nums[last_non_duplicate]
    return last_non_duplicate + 1
        
```
# Solution #2
change line 10 to 
```python
nums[last_non_duplicate] = nums[i]
```

## Explanation
The goal here is to return the number of non duplicates by modifying the array. 
