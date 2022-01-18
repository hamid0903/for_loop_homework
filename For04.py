def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    idx=[]
    for i in range(A,B):
        idx.append(i)
    return idx
print(main(0,5))