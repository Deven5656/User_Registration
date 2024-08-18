'''
    @Author: Deven Gupta
    @Date: 17-08-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 17-08-2024 
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

def validate_user(first_name, last_name):
    """
    Description:
        This function is use to call other functions
    Parameters:
        first_name (str): First name of user
        last_name (str): Last name of user
    Returns:
        tuple : containing boolean values
    """
    valid_first = is_valid_name(first_name)
    valid_last = is_valid_name(last_name)
    return valid_first, valid_last


def main():
        
    logger=create_logger('Validate_logger')

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    valid_first, valid_last = validate_user(first_name, last_name)

    if valid_first:
        print(f"First Name: '{first_name}' - Valid")
    else:
        print(f"First Name: '{first_name}' - Invalid")

    if valid_last:
        print(f"Last Name: '{last_name}' - Valid")
    else:
        print(f"Last Name: '{last_name}' - Invalid")
    
    logger.info("Information is Validated")
   
if __name__ == "__main__":
    main()

