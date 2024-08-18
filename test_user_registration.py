'''
    @Author: Deven Gupta
    @Date: 17-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 17-08-2024 
    @Title : TestCase

'''

import unittest
from user_registration import is_valid_name


class TestUserValidation(unittest.TestCase):

    def test_is_valid_name(self):
  
        self.assertTrue(is_valid_name("Alice"))
        self.assertTrue(is_valid_name("Bob"))

        self.assertFalse(is_valid_name("alice"))
        self.assertFalse(is_valid_name("Al"))
        self.assertFalse(is_valid_name("Alicia123"))


if __name__ == "__main__":
    unittest.main()
