def chop(t):
    """
    Takes a list and modifies it, removing the first and last elements, 
    and returns None.
    """
    if len(t) > 0:
        t.pop(0)
    if len(t) > 0:
        t.pop(-1)
    return None

def middle(t):
    """
    Takes a list and returns a new list that contains all but the 
    first and last elements.
    """
    return t[1:-1]

# Testing Exercise 1
if __name__ == "__main__":
    # Test chop
    my_list = [1, 2, 3, 4]
    print(f"Original list for chop: {my_list}")
    result_chop = chop(my_list)
    print(f"After chop: {my_list}")
    print(f"Result of chop (should be None): {result_chop}")

    # Test middle
    my_list_2 = [1, 2, 3, 4]
    print(f"\nOriginal list for middle: {my_list_2}")
    new_list = middle(my_list_2)
    print(f"New list from middle: {new_list}")
    print(f"Original list after middle (should be unchanged): {my_list_2}")
