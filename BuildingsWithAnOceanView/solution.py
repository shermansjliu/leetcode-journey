


def solution(heights):

    '''
    
    Brute force
    For each element
    Scan bulidings to the right and add to an array
    sort the array

    keep track of lef tmax

    max_h = float('-inf')
    for i in len(heights) -1 --> 0:
        
        if heights[i] < max_h:
            building has ocean view
        max_h = max(heights[i], max_h) 
        
    sort 
    '''
    res = []
    max_h = float('-inf')
    for i in range(len(heights)-1, -1, -1):
        if heights[i] > max_h:
            res.append(i)
        max_h = max(heights[i], max_h)
    
    res.sort()
    
    return res



def tests():
    print(solution([4,2,3,1]))

    print(solution([4,3,2,1]))

    print(solution([1,3,2,4]))
    print(solution([2,2,2,2]))

if __name__ == '__main__':
    tests()