# Solution 1 Brute Force

def subarraySum(self, nums: List[int], k: int) -> int:

## Explanation

- For a single element
  - Make each subsequent element be an 'end'
  - Increment the starting pointer by 1 each time to capture all subarrays in between.

## Run Time

- O(n^3)
- For each element a n^2 operation is executed.

## Space Complexity

- O(1)

# Solution 2 Dynamic Programming

## Key Idea

- Let's define a running_sum for element, R[i] as the sum from 0 -> i inclusive. E.g A[1,3,4]: R[0] = 1, R[1] = 4, R[2] = 8
- Given a two running sums, R[i], R[j] if R[i] - R[j] = k for i > j, means there exits a contigous A[j+1:i+1] subarray that adds up to k. Try a few examples.
- Nowe have an equation R[i] - R[j] = k
- We know R[j] might be a cumulative subarray encountered before, but we don't know.
- Thus, store every cumulative summ we come across to check against later. I.e the R[i] we look at now, should become the R[j] for future elements in R.

```python
    def subarraySum(self, nums: List[int], k: int) -> int:

        #Note that we'll never get a running sum of 0, so we need to include it. I.e if a subarray is [k]
        prev_running_sums = {0:1}
        running_sum_i = 0 #R[i]  can be stored with an integer, we just need to add the current element at every iteration
        count = 0

        for i in range(len(nums)):
            cumulative_sum += nums[i]
            running_sum_j = cumulative_sum - k
            if running_sum_j in prev_running_sums:
                count += prev_running_sums[running_sum_j] #Checking if running_sum_j's exist
            prev_running_sums[cumulative_sum] = prev_running_sums.get(cumulative_sum, 0) + 1 #Store running_sum_i for future elements

        return count
```

## Run Time

- 1 pass thorugh the list n
- n checks of constant time into the prev_running_sums dictionary
- Thus, O(n)

## Space Complexity

- Create a new dictionary that potentially stores a unique running sum for each element
- O(n)
