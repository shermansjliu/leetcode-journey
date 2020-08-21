# Solution
```python
def hasCycle(self, head: LinkedList)-> bool:
  slow = head
  fast = head
  while fast.next and fast.next.next: #To check for even and odd
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return True

```


### Explanation
- Intuitively, if there are two runners on track and one runner is faster than the other.
- If the track is ciruclar the faster runner will eventually meet up with the slow runner
- If the track is not circular the runner will finish the race

## Running time and Space time
n is the number of nodes 
O(n)