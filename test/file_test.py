import unittest
import sys
sys.path[0] = "C:\\Users\\cobyl\\Documents\\Coding\\MicrosoftCode\\ActualDevelopment"

class TestFileFunctions(unittest.TestCase):
    def test_read_file(self):
        from PythonQuickStartModule.src import File
        File.ReadFile("C:\\Users\\cobyl\\Documents\\Coding\\MicrosoftCode\\ActualDevelopment\\data.txt")

if __name__ == '__main__':
    unittest.main()