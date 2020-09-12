""" This file will store all the functions about managing Lists
"""

import sys

def ListToStr(List):
    """This function will turn a list into a string

    Args:
        List (List): The list you want converted into str

    Returns:
        str: The list as a string
    """

    NewString = ""
    for ListItem in List:
        try:
            NewString += ListItem
        except TypeError:
            try:
                ListItem = str(ListItem)
                NewString += ListItem
            except:
                sys.exit("The vairiable: {}. Is not a str and cannot be converted into str."
                .format(NewString))
    
    return NewString