###PURPOSE : some general purposes function
import pdb



def becomes_list(a):
    """Return the input as a list if it is not yet"""

    if isinstance(a,list):
        return a
    else:
        return [a]


def add_to_list(list1, new_element):
    """Concatenate new_element to a list

    Parameters:
    ----------
    list1: list
        Must be a list
    new_element : any
        new element to be added at the end of list1

    Output:
    ------
    result: list
        1D list
    """
    return list1+becomes_list(new_element)
        


def is_type(a,type):
    """Test if each element of list is of a given type"""
    return [isinstance(i,type) for i in a]

