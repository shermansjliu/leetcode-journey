# Solution 1 Kadane's Algorithm

## Key idea / observation

- The maximum cotniguous subarray of A[i] = max(A[i], A[i] - A[i-1])
- The choice here is: continue to build off the maximum contiguous subarray or start new contiguous subarray

### Why is this true?

- Take the example array [-2,1,-3,4,-1,2,1,-5,4]
- THe max subarray of [-2] is simply[-2]
- The max subarray of [-2,1] is the sum of all the elements: -2 + 1, or 1
- The maximum subarray of [-2,1,-3]
  - Our choices are:
  - -3 = -3
  - -3 + 1 = -2
  - -2 + 1 - 3 = -4
- There's no point in checking (-2 + 1 - 3) because we alerady know the maximum subarray sum from A[0:1] is 1
- for A[-2,1,-3,4]
- We could either check all the subarrays in A[0:3], but since we already have the maximum subarray sum in A[0:3] from our previous calculation, we only need to check if starting a new subarray is more optimal or building off our previous contiguous subarray.

```python
def maximumSubarray(nums:List[int])-> int

```

## Explanation

## Run Time

## Space Complexity

# Solution 2 Divide and Conquer

## Key idea / observation

## Key Idea

## Explanation

## Run Time

## Space Complexity
