def solution(inputArray):
    """Strategy 1: Math Trick
    Runtime: O(kn) where k is the max integer of inputArray

    Args:
        inputArray (List[int]) : list of obstacles

    Returns:
        int: length to jump
    """
    largest = max(inputArray)
    for i in range(1,largest+1):
        divs = any(x % i == 0 for x in inputArray)
        if not divs:
            return i
    return largest+1

