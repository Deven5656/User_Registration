'''
    @Author: Deven Gupta
    @Date: 18-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 18-08-2024 
    @Title : Python program for User Registration Problem

'''

import re
from logger import create_logger

def is_valid_name(name):
    """
    Description:
        This function is use to match the pattern in name
    Parameters:
        name (str): name of user
    Returns:
        boolean : True if match else False
    """
    pattern = r'^[A-Z][a-zA-Z]{2,}$'
    return bool(re.match(pattern, name))

def is_valid_email(email):
    """
    Description:
        This function is use to match the pattern in email
    Parameters:
        email (str): mail of user
    Returns:
        boolean : True if match else False
    """

    pattern = r'^[a-zA-Z0-9._%+-]+(?:\.[a-zA-Z0-9._%+-]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_mobile(mobile):
    """
    Description:
        This function is use to match the pattern in mobile number
    Parameters:
        mobile (str): mobile number of user
    Returns:
        boolean : True if match else False
    """
 
    pattern = r'^\d{2} \d{10}$'
    return bool(re.match(pattern, mobile))


def validate_user(first_name, last_name, email, mobile):
    """
    Description:
        This function is use to call other functions
    Parameters:
        first_name (str): First name of user
        last_name (str): Last name of user
        email (str) : mail of user
        mobile (str): mobile number of user
    Returns:
        tuple : containing boolean values
    """
    valid_first = is_valid_name(first_name)
    valid_last = is_valid_name(last_name)
    valid_email = is_valid_email(email)
    valid_mobile = is_valid_mobile(mobile)
    return valid_first, valid_last, valid_email, valid_mobile


def main():
        
    logger=create_logger('User_Registration')

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    mobile = input("Enter your mobile number (e.g., 91 9765859088): ")
    
    valid_first, valid_last, valid_email, valid_mobile = validate_user(first_name, last_name, email, mobile)

    if valid_first:
        logger.info(f"First Name: '{first_name}' - Valid")
    else:
        logger.info(f"First Name: '{first_name}' - Invalid")

    if valid_last:
        logger.info(f"Last Name: '{last_name}' - Valid")
    else:
        logger.info(f"Last Name: '{last_name}' - Invalid")

    if valid_email:
        logger.info(f"Email: '{email}' - Valid")
    else:
        logger.info(f"Email: '{email}' - Invalid")

    if valid_mobile:
        logger.info(f"Mobile: '{mobile}' - Valid")
    else:
        logger.info(f"Mobile: '{mobile}' - Invalid")
    
   
if __name__ == "__main__":
    main()

