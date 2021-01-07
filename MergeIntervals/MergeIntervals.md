# Opitmal Solution: Sort
## Key Insight

- Assume The intervals are sorted by starting time. 
- Suppose there is an overlap between i and j (j = i + 1), let start_opt and end_opt be the merged intervals 
    - we know start_opt = start_i (since we sorted by start time)
    - Since there is an overlap, start_j <= end_i So we ignore start_j
    - We make end_opt = max(end_j, end_i) because end time is not sorted 
- [[1,3],[2,6],[8,10],[15,18]] --> [[1,6],[8,10],[15,18]]
- [[1,4], [1,3]] --> [1,4] (end time is not sorted)
- If there is no overlap start_j > end_i, just add interval[i]

```python
    #Note: lst[-1] means getting the last element of the list
    #So interval[i][-1] = interval[i][1]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(len(intervals)):
            if not res or res[-1][-1] < intervals[i][0]:
                res.append(intervals[i])
            else: 
                res[-1][-1] = max(res[-1][-1], intervals[i][-1])
        return res
    
```
## Run Time 
- let n be length of *intervals*
- Sorting the array O(nlogn)
- Iterating over *intervals* O(n)
- Overall time complexity = O(nlogn)
## Space Complexity
- New array to store intervals. 
- Worst case input: No overlapping intervals O(n), so all elements in intervals must be added