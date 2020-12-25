# Solution 1 Brute Force

```python

```

## Explanation

- For a single element
  - Make each subsequent element be an 'end'
  - Increment the starting pointer by 1 each time to capture all subarrays in between.

## Run Time

## Space Complexity

# Solution 2 Sliding Window

## Key Idea

- Let s be the sum we are trying to target.
- Suppose our subarrays are between two pointers start and end. I.e the subarray will be A[start:end+1]
- Because there are only positive nubmers in the array, everytime we increase the size of A[start:end+1], we increase the sum
- Similarly, everytime we decrease the size of A[start:end+1] we decrease the **s**.
- Thus, if A[start:end+1] is below the **s**, we should increment 'end' and if A[start:end+1] is >= **s**.
- Once A[start:end+1] is >= **s** we should try to decrement l as much as possible to get the minimum sum

### Example

- A = [1,1,2,5], s = 5
- let start, end = 0
- Incremenet r until our subarray = A because 1+1+2 < 5
- Now, since 1 + 1 + 2 + 5 >= 5, let's try to discard as many numbers as possible while still keeping the sum of A[start:end+1] >= s

```python
def minSubArrayLen(s: int, nums: List[int]) -> int:
    res = float('inf')
    l = 0
    r = 0

    while r < len(nums):
        subarr_sum = sum(nums[l:r+1])
        if subarr_sum >= s:
            while subarr_sum >= s:
                l += 1
                subarr_sum = sum(nums[l:r+1])
            res = min(res, len(nums[l-1:r+1]))
        r += 1

    if res == float('inf'):
        return 0
    return res
```

## Run Time

- O(n) Two pointers, one traversal through the array

## Space Complexity

- O(1) We only instantiated new integers and floats which does not depend on the size of the input.
