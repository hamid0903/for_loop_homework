def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    idx=""
    for i in range(n):
        if i<n:
            s=idx+str(i)
    return (s)
print(main(5))