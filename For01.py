import py_compile
from re import X


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    list1=[]
    for i in range(n):
        list1.append(i)
    return list1
print(main(10))