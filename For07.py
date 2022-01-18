def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    idx=0
    N+=1
    for i in range(1,N,2):
        idx+=i
    return idx
print(main(5))