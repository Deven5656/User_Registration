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
        # Valid names
        self.assertTrue(is_valid_name("Gupta"))
        self.assertTrue(is_valid_name("Bhoir"))

        # Invalid names
        self.assertFalse(is_valid_name("gupta"))
        self.assertFalse(is_valid_name("DG"))
        self.assertFalse(is_valid_name("Gupta123"))


if __name__ == "__main__":
    unittest.main()
