```python
    def isHappy(self, n: int) -> bool:
        
        seened_numbers = set()
        def getSumSquares(n):
            result = 0
            n_str = str(n)
            
            for char in n_str:
                result += int(char) ** 2
            return result
                
           
        while True:
            sum_squares = getSumSquares(n)
            print(sum_squares)
            if sum_squares == 1:
                return True
            elif sum_squares in seened_numbers:
                return False
            else:
                seened_numbers.add(sum_squares)
                n = sum_squares

```

# Key Ideas
- Certain square combinations of digits will result in a cycle, which causes an infinite loop
- Therefore, by keeping track of summed squares will help us identify when a particular number will loop endlessly
- Use a set so that chceking takes constant time

