# Solution #1

```python
 for i in range(len(nums)-1, -1, -1):
            if nums[i]== 0:
                j = i
                while j + 1 <= len(nums)-1 and nums[j+1] != 0:
                    nums[j],nums[j+1] = nums[j+1], nums[j]
                    j+= 1
```

## Explanation

Goal: Move all the zeroes to one side and keep the relative ordering.
When I see a 0 in the list, I want to keep swap its right adjacent element to bubble the 0 to the end while maintaining the order of the list. If the right adjacent element is a 0, I don't need to bubble the current 0 any further along the list.

# Solution #2

```python
def moveZeroes(self, nums: List[int]) -> None:
    if len(nums) == 0:
        return
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
    for i in range(len(nums), last_non_zero):
        nums[i] = 0
```

## Explanation (IPR)
Instead of swapipng l