from re import X


def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    idx=0
    N+=1
    for i in range(1,N):
        idx+=1/i
    return idx
print(main(5))
x=1+1/2+1/3+1/4+1/5
print(x)