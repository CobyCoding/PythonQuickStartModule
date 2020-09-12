import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("PythonQuickStartModule"), '..')))

class TestListFunctions(unittest.TestCase):
    def test_list_to_str(self):
        from PythonQuickStartModule.src import Lists
        Lists.ListToStr(["hi", "hi", "general"])

if __name__ == '__main__':
    unittest.main()