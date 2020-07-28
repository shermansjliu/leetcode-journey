```python
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
  dct1 = dict()
  dct2 = dict()
  intersection = []
  for num2 in nums2:
      if not dct2.get(num2):
          dct2[num2] = 1
      else:
          dct2[num2] += 1
  for num1 in nums1:
      if not dct1.get(num1):
          dct1[num1] = 1
      else:
          dct1[num1] += 1
  smaller = nums2
  if len(nums1) < len(nums2):
      smaller = nums1
  for key in dct1.keys():
      if dct2.get(key):
          if dct2[key] < dct1[key]:
              for i in range(dct2.get(key)):
                  intersection.append(key)
          else:
              for j in range(dct1.get(key)):
                  intersection.append(key)
  return intersection

```

# Key Ideas
- This approach finds the intersection by comparing every single element in a list to another list. 
- Reduce look-up time by strong the number and freqeuncy in a dictionary where an element in a list key and its corresponding frequency is the value
- After nums1 and nums2 are stored in corresponding dictionaries, a small optimiziation is to always iterate over the list with the least number of elements
## Run Time
- Let *m* be the length of nums1 and *n* be the length of nums2
- Creating *dct1* and *dct2* is O(n + m)
- The outer for loop is O(smaller list)
- The inner for loop iterates over each element in the smaller list O(smaller list)
- n + m is always >= n or m
- Run time is O(n + m)
