import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("PythonQuickStartModule"), '..')))

class Error(Exception):
    def __init__(self, ErrorMessage):
        print(ErrorMessage)

class TestStringFunctions(unittest.TestCase):
    def test_readfile(self):
        from PythonQuickStartModule.src import Strings
        Strings.RemoveNewLine("\nhi\n")
        

if __name__ == '__main__':
    unittest.main()