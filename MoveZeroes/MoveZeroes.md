# Solution #1
```python
def moveZeroes(self, nums: List[int]) -> None:
    if len(nums) == 0:
        return
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
```
## Explanation
To move all zeros to the right, swap position of non-zero numbers with 0s 
When a non-zero number is reached, it is swapped with the position of 'last_non_zero'. Everything before 'last_non_zero' is a non-zero number. Since the loop iteratives from the start of the list to the end, relative ordering is maintained
