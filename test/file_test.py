import unittest
import sys
sys.path[0] = "C:\\Users\\cobyl\\Documents\\Coding\\MicrosoftCode\\ActualDevelopment"

class TestFileFunctions(unittest.TestCase):
    def test_read_file(self):
        from PythonQuickStartModule.src import File
        File.ReadFile("PythonQuickStartModule\\test\\data.txt")
        File.ReadFile("PythonQuickStartModule\\test\\data.txt", False)
    
    def test_list_to_file(self):
        from PythonQuickStartModule.src import File
        File.ListToFile(["Hi", "Whats Up", 1, 2], "PythonQuickStartModule\\test\\data.txt")
        File.ListToFile(["Hi", "Whats Up", 1, 2], "PythonQuickStartModule\\test\\data.txt", False)

if __name__ == '__main__':
    unittest.main()