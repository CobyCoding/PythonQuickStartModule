import unittest
import sys
sys.path[0] = "C:\\Users\\cobyl\\Documents\\Coding\\MicrosoftCode\\ActualDevelopment"

class TestStringFunctions(unittest.TestCase):
    def test_readfile(self):
        from PythonQuickStartModule.src import Strings
        Strings.RemoveNewLine("\nhi\n")

if __name__ == '__main__':
    unittest.main()