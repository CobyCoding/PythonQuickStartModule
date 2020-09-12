""" This file will store all the functions about
managing files

"""
import sys
from PythonQuickStartModule.src import Strings


def ReadFile(path, RemoveNewLine=True):
    """This will read a file

    Args:
        path (str): The path of the file you want read.
        RemoveNewLine (bool, optional): If you want to remove the \n from the lines. Defaults to True.

    Returns:
        list: The lines of the file
    """ 
    
    try:
        with open(path) as f:
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