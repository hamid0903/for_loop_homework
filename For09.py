def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    idx=[]
    
    for i in range(1,11):
        idx.append(price*i)
    return idx
print(main(2.5))