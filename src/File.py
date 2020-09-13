""" This file will store all the functions about
managing files

It can be imported via:

from PythonQuickStartModule.src import Files
"""

import sys
from PythonQuickStartModule.src import Strings


def ReadFile(path, RemoveNewLine=True):
    """This will read a file

    Args:
        path (str): The path of the file you want read.
        RemoveNewLine (bool, optional): If you want to remove the \\n from the lines. Defaults to True.

    Returns:
        list: The lines of the file
    """ 

    try:
        with open(path, "r") as f:
            try:
                lines = f.readlines()
            except:
                sys.exit("The file can not be read.")

    except FileNotFoundError:
        sys.exit("The path {} does not exist.".format(path))
    
    if RemoveNewLine:
        for line in lines:
            lines[lines.index(line)] = Strings.RemoveNewLine(line)

    else:
        return lines
    
    return lines

def ListToFile(List, path, AddNewLine = True):

    """This function will take a list and write each item into a file

    Args:
        List (list): The list you want written in.
        path (str): The path of the file.
        AddNewLine (bool, optional): If you want a new line between each item. Defaults to True.
    """

    for x in range(0, len(List)):
        try:
            List[x] = str(List[x])
        except:
            sys.exit("Please make sure you passed in a list that only contains str and ints. If you are sure you did you can make a issue report on our github: https://github.com/CobyCoding/PythonQuickStartModule")
    try:
        with open(path, "a+") as f:
            try:
                for line in List:
                    f.write(line + "\n" if AddNewLine else line)
            except:
                sys.exit("Please make sure you passed in a list. If you are sure you did you can make a issue report on our github: https://github.com/CobyCoding/PythonQuickStartModule")

    except FileNotFoundError:
        sys.exit("The path {} does not exist".format(path))
