import unittest
import os
from a_createfield import create

class Test_create_function(unittest.TestCase):

    def setUp(self) -> None:
        self.file_path =create()
        return super().setUp()
    
    def tearDown(self) -> None:
        if os.path.exists(self.file_path):
           os.remove(self.file_path)
        return super().tearDown()
    
    def test_create_funtion(self):
        self.assertTrue(os.path.isfile(self.file_path))

if __name__=="__main__":
    unittest.main()