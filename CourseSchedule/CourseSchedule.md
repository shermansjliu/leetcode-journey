# Solution 1

```python
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
    '''
    Convert edge list to a adjacency list. This is so that access
    '''
      adj_list = [[] for i in range(numCourses)]
      
      for x,y in prerequisites:
          adj_list[x].append(y)
      '''
      Store states of nodes. We use a list because the vertex is represented as a number, which can be used to index a position in a list in constant time
      '''
      visit_state = [0]*numCourses

      def hasCycle(v)->bool:
          '''
          If the vertex has been explored: There is no cycle
          '''
          if visit_state[v] == 2:
              return False

          '''
          If a vertex has been visited and one of it's neighbors has come across it again, there is a cycle
          E.g [A, B], [B, A]
          1. hasCycle(A)
          2. visit_state[A] = 1
          3. hasCycle(B)
          4. Since visit_state[A] is 1, we know there is a cycle
          '''
          if visit_state[v] == 1:
              return True
         
          visit_state[v] = 1

          for neighbor in adj_list[v]:
              if hasCycle(neighbor):
                  return True
        
          visit_state[v] = 2
          return False
      
      for v in range(numCourses):
          if hasCycle(v):
              return False
      return True
```

## Key Ideas
 * The goal is to detect wheter there is a cycle in the graph because a cycle cannot exist in a course schedule. E.g It does not make sense for Math101 to require Math102 and Math102 to require Math101.
 * The edge list is first converted to an adjecency list because it makes accessing neighbors much easier
 * A vertex in the graph is in one of three states
  1. Unvisited - The vertex has yet to be visited by our algorithm
  2. Visited -  The vertex has been visited but NOT all of its descendents have been explored
  3. Explored - The vertex has been visited and all of its descendents have been explored


