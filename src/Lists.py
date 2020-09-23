""" This file will store all the functions about managing Lists

It can be imported via:

from PythonQuickStartModule.src import Lists
"""

import sys

def ListToStr(List, split=None):
    """This function will turn a list into a string

    Args:
        List (List): The list you want converted into str

    Returns:
        str: The list as a string
    """

    NewString = ""
    for ListItem in List:
        try:
            if split:
                if not List[-1] == ListItem:
                    NewString += ListItem + split
                else:
                    NewString += ListItem
            else:
                NewString += ListItem
        except TypeError:
            try:
                ListItem = str(ListItem)
                NewString += ListItem
            except:
                sys.exit("The vairiable: {}. Is not a str and cannot be converted into str."
                .format(NewString))
    
    return NewString