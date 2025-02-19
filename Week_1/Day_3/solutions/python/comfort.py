def closed_brackets(s):
    min_open = 0
    max_open = 0
    for char in s:         
    
        if char == '(':
            min_open += 1
            max_open += 1
        elif char == ')':
            min_open -= 1
            max_open -= 1
        elif char == 'J':
            min_open -= 1
            max_open += 1
        min_open = max(min_open , 0)
        
        if max_open < 0:
            return False
    
    return min_open == 0