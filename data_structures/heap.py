import random
class heap:
    '''
    min heap
    '''
    def __init__(self) -> None:
        self.h = []

    def peek(self):
        if len(self.h) > 0:
            return 0
        return self.h[0]

    def insert(self, val):
        '''
        insert <val> to the last availalbe sapce and swap the val with it's parent if val > parent

        '''
        self.h.append(val)
        idx = len(self.h)-1
        parent_idx = (idx-1)//2
        while parent_idx >= 0 and self.h[idx] < self.h[parent_idx]:
            '''
            Parent < sibling, so if new element is < parent. then new element < sibling 
            '''
            self.h[idx], self.h[parent_idx] = self.h[parent_idx], self.h[idx]
            idx = parent_idx
            parent_idx = (idx-2)//2
            
    def pop(self):
        '''
        Swap last element with root 
        remove last element 
        bubble new root element down 

        
        '''
        n = len(self.h)
        self.h[0], self.h[n-1] = self.h[n-1], self.h[0]
        popped_element = self.h.pop(-1)
        self._bubble_down()
        
        return popped_element
    def _bubble_down(self):
        idx = 0
        n = len(self.h)
        left_child_idx = (2*idx) +1
        while left_child_idx < n:
            
            smaller_child_index = left_child_idx 
            right_child_idx = (2*idx) +2
            if n > right_child_idx:
                if self.h[right_child_idx] < self.h[smaller_child_index]:
                    smaller_child_index = right_child_idx
            if self.h[idx] < self.h[smaller_child_index]:
                break
            self.h[idx], self.h[smaller_child_index] = self.h[smaller_child_index], self.h[idx]
            idx = smaller_child_index 
            left_child_idx = (2*idx) +1 
            
            
_heap = heap()
vals = [3,4,8,9,7,10,9, 15,20,13] 
for v in vals:
    _heap.insert(v)
print(_heap.h)
print(_heap.pop())
print(_heap.h)
        
