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
## Key Ideas
- Swap the positions of non-zero numbers in the array with 0s in the array
- Maintain relative ordering by keeping track of the right most non-zero number

# Solution #2
```python
def moveZeroes(self, nums: List[int]) -> None:
    if len(nums) == 0:
        return
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1

    for i in range(last_non_zero+1, len(nums)):
        nums[i] = 0
```
- Duplicate all non zero numbers to the beginning of the list
- Everything after the right most non-zero number should be a  0
