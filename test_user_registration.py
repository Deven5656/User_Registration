'''
    @Author: Deven Gupta
    @Date: 20-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 20-08-2024 
    @Title : TestCase

'''

import unittest
from user_registration import is_valid_name, is_valid_email, is_valid_mobile, is_valid_password


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

        #Additional Testcases
        # Valid
        self.assertTrue(is_valid_email("abc@yahoo.com"))           
        self.assertTrue(is_valid_email("abc-100@yahoo.com"))       
        self.assertTrue(is_valid_email("abc.100@yahoo.com"))       
        self.assertTrue(is_valid_email("abc111@abc.com"))          
        self.assertTrue(is_valid_email("abc111@abc.net"))          
        self.assertTrue(is_valid_email("abc.100@abc.com.au"))     
        self.assertTrue(is_valid_email("abc@1.com"))               
        self.assertTrue(is_valid_email("abc@gmail.com.com"))       
        self.assertTrue(is_valid_email("abc+100@gmail.com"))

        # Invalid
        self.assertFalse(is_valid_email("abc"))                  
        self.assertFalse(is_valid_email("abc@.com.my"))         
        self.assertFalse(is_valid_email("abc123@gmail.a"))       
        self.assertFalse(is_valid_email("abc123@.com"))          
        self.assertFalse(is_valid_email("abc123@.com.com"))     
        self.assertFalse(is_valid_email(".abc@abc.com"))         
        self.assertFalse(is_valid_email("abc()*@gmail.com"))    
        self.assertFalse(is_valid_email("abc@%*.com"))           
        self.assertFalse(is_valid_email("abc..2002@gmail.com"))   
        self.assertFalse(is_valid_email("abc.@gmail.com"))       
        self.assertFalse(is_valid_email("abc@abc@gmail.com"))    
        self.assertFalse(is_valid_email("abc@gmail.com.1a"))     
        self.assertFalse(is_valid_email("abc@gmail.com.aa.au"))

    def test_is_valid_mobile(self):
        # Valid mobile numbers
        self.assertTrue(is_valid_mobile("91 9765859088"))
        self.assertTrue(is_valid_mobile("91 1234567899"))

        # Invalid mobile numbers
        self.assertFalse(is_valid_mobile("919765859088"))
        self.assertFalse(is_valid_mobile("91 992233778"))
        self.assertFalse(is_valid_mobile("91 12345678910"))

    def test_is_valid_password(self):
        # Valid passwords
        self.assertTrue(is_valid_password("Password@123"))
        self.assertTrue(is_valid_password("Pass$1223"))
        self.assertTrue(is_valid_password("Pass#TF12"))

        # Invalid passwords
        self.assertFalse(is_valid_password("Password@"))
        self.assertFalse(is_valid_password("Password@#123"))
        self.assertFalse(is_valid_password("Validpass123"))



if __name__ == "__main__":
    unittest.main()
