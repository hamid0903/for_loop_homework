def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    idx=[]
    for i in range(n):
        idx.append(k)        
    return idx
print(main(5,3))