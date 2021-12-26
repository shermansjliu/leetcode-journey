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
        bubble = True
        while bubble:
            left_child_idx = (2*idx) +1
            right_child_idx = (2*idx) +2
            if n > left_child_idx and n > right_child_idx: #if left and right child exists 
                pass
                #if greather than any child, swap with the minumum 
                if self.h[left_child_idx] < self.h[idx] and self.h[left_child_idx] < self.h[right_child_idx]:
                    pass #swap with left child
                    self.h[idx], self.h[left_child_idx] = self.h[left_child_idx], self.h[idx]
                    idx = left_child_idx
                    bubble = True
                    continue

                elif self.h[right_child_idx] < self.h[idx] and self.h[right_child_idx] < self.h[left_child_idx]:
                    pass #swap with right child 
                    self.h[idx], self.h[right_child_idx] = self.h[right_child_idx], self.h[idx]
                    idx = right_child_idx
                    bubble = True
                    continue

            # if only left child exists 
            elif n > left_child_idx:
                if self.h[idx] > self.h[left_child_idx]:
                    self.h[idx], self.h[left_child_idx] = self.h[left_child_idx], self.h[idx]
                    idx = left_child_idx
                    bubble = True
                    continue 
            bubble = False
            # if only right child exists Not possible same with no children 
            
            
            
            
_heap = heap()
vals = [3,4,8,9,7,10,9, 15,20,13] 
random.shuffle(vals)
for v in vals:
    _heap.insert(v)
print(_heap.h)
print(_heap.pop())
print(_heap.h)
        
