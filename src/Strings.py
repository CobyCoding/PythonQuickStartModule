import sys
from PythonQuickStartModule.src import Lists

def RemoveNewLine(string):
    try:
        stringList = list(string)
    except TypeError:
        sys.exit("The vairiable: {} is not a str".format(string))

    try:
        stringList.remove("\n")
    except:
        return string
    
    return Lists.ListToStr(stringList)