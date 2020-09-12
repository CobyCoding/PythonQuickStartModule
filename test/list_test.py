import unittest
import sys
sys.path[0] = "C:\\Users\\cobyl\\Documents\\Coding\\MicrosoftCode\\ActualDevelopment"

class TestListFunctions(unittest.TestCase):
    def test_list_to_str(self):
        from PythonQuickStartModule.src import Lists
        Lists.ListToStr(["hi", "hi", "general"])

if __name__ == '__main__':
    unittest.main()