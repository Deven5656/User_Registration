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


def validate_user(first_name, last_name, email):
    """
    Description:
        This function is use to call other functions
    Parameters:
        first_name (str): First name of user
        last_name (str): Last name of user
        email (str) : mail of user
    Returns:
        tuple : containing boolean values
    """
    valid_first = is_valid_name(first_name)
    valid_last = is_valid_name(last_name)
    valid_email = is_valid_email(email)
    return valid_first, valid_last, valid_email


def main():
        
    logger=create_logger('Validate_logger')

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    
    valid_first, valid_last, valid_email = validate_user(first_name, last_name, email)

    if valid_first:
        print(f"First Name: '{first_name}' - Valid")
    else:
        print(f"First Name: '{first_name}' - Invalid")

    if valid_last:
        print(f"Last Name: '{last_name}' - Valid")
    else:
        print(f"Last Name: '{last_name}' - Invalid")

    if valid_email:
        print(f"Email: '{email}' - Valid")
    else:
        print(f"Email: '{email}' - Invalid")
    
    logger.info("Information is Validated")
   
if __name__ == "__main__":
    main()

