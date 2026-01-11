def solution(inputString):
    """Strategy 1: stack
    Runtime: O(kn) where k is the # of stack parenthese
    Space: O(n)

    Args:
        inputString (str): string to be reverse in parentheses

    Returns:
        str: string reversed in parentheses
    """
    n = len(inputString)
    result, word = "", ""
    stack =[]
        
    for i in range(n):
        if inputString[i] == "(":
            if word != "":
                stack.append(word)
            stack.append("(")
            word = ""
        elif inputString[i] == ")":
            while stack[-1] != "(":
                word = stack.pop() + word
            stack.pop()
            stack.append(word[::-1])
            word = ""
        else:
            word += inputString[i]
    
    stack.append(word)
    
    while stack:
        result = stack.pop() + result
    return result
            

