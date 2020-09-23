import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("PythonQuickStartModule"), '..')))

class TestFileFunctions(unittest.TestCase):
    def test_get_coloe(self):
        from PythonQuickStartModule.src import Color
        Color.GetColor("red")


if __name__ == '__main__':
    unittest.main()