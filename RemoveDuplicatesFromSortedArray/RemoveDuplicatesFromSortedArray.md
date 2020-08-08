# Solution #1

```python
def removeDuplicates(self, nums: List[int]) -> None:
    if len(nums) == 0 or is None:
        return 0
    last_non_duplicate = 0
    for i in range(1, len(nums)):
        if nums[last_non_duplicate] != nums[i]
        last_non_duplicate += 1
        nums[last_non_duplicate], nums[i] = nums[i], nums[last_non_duplicate] #Or simply nums[last_non_duplicate] = nums[i]
        
        
    return last_non_duplicate + 1
        
```
## Explanation
- Every encounter with a different number means the number of distinct elements increases by 1
- Modify the array by using a tracker to denote the last element you switched/changed


 
