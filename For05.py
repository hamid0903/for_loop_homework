def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    A-=1
    idx=[]
    for i in range(B,A,-1):
        idx.append(i)
    return idx
print(main(0,5))