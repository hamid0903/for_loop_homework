def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    idx=0
    B+=1
    for i in range(A,B):
        idx+=i
    return idx
print(main(0,5))
