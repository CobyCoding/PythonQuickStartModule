""" This file will store all the functions about
managing files

"""
import sys
from PythonQuickStartModule.src import Strings


def ReadFile(path, RemoveNewLine=True):
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