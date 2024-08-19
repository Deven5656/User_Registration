'''
    @Author: Deven Gupta
    @Date: 18-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 18-08-2024 
    @Title : TestCase

'''

import unittest
from user_registration import is_valid_name, is_valid_email, is_valid_mobile


class TestUserValidation(unittest.TestCase):

    def test_is_valid_name(self):
        # Valid names
        self.assertTrue(is_valid_name("Gupta"))
        self.assertTrue(is_valid_name("Bhoir"))

        # Invalid names
        self.assertFalse(is_valid_name("gupta"))
        self.assertFalse(is_valid_name("DG"))
        self.assertFalse(is_valid_name("Gupta123"))

    def test_is_valid_email(self):
        # Valid emails
        self.assertTrue(is_valid_email("devengupta0987@gmail.com"))
        self.assertTrue(is_valid_email("dev.gupta@gmail.co.in"))

        # Invalid emails
        self.assertFalse(is_valid_email("deven.gupta@.com"))
        self.assertFalse(is_valid_email("dev.123@in"))
        self.assertFalse(is_valid_email("dev.09gupta@.com"))

    def test_is_valid_mobile(self):
        # Valid mobile numbers
        self.assertTrue(is_valid_mobile("91 9765859088"))
        self.assertTrue(is_valid_mobile("91 1234567899"))

        # Invalid mobile numbers
        self.assertFalse(is_valid_mobile("919765859088"))
        self.assertFalse(is_valid_mobile("91 992233778"))
        self.assertFalse(is_valid_mobile("91 12345678910"))



if __name__ == "__main__":
    unittest.main()
