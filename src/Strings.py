import sys
from PythonQuickStartModule.src import Lists

def RemoveNewLine(string):
    """This function will remove the \n from a string

    Args:
        string (str): The string you want the \n removed from

    Returns:
        str: The string you passed in without the \n
    """
    try:
        stringList = list(string)
    except TypeError:
        sys.exit("The vairiable: {} is not a str".format(string))

    try:
        stringList.remove("\n")
    except:
        return string
    
    return Lists.ListToStr(stringList)