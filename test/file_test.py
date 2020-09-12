import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("PythonQuickStartModule"), '..')))

class TestFileFunctions(unittest.TestCase):
    def test_read_file(self):
        from PythonQuickStartModule.src import File
        File.ReadFile("test\\data.txt")
        File.ReadFile("test\\data.txt", False)
    
    def test_list_to_file(self):
        from PythonQuickStartModule.src import File
        File.ListToFile(["Hi", "Whats Up", 1, 2], "test\\data.txt")
        File.ListToFile(["Hi", "Whats Up", 1, 2], "test\\data.txt", False)

if __name__ == '__main__':
    unittest.main()