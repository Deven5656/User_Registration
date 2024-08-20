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

def is_valid_password(password):
    """
    Description:
        This function is use to match the pattern in email
    Parameters:
        password (str): password of user
    Returns:
        boolean : True if match else False
    """
    pattern=r"^.{8,}$"
    return bool(re.match(pattern, password))

def valid_input(input_msg, validation_func, error_msg):
    """
    Description:
        This function repeatedly takes the user input until the input passes the valid 
    Parameters:
        input_msg (str): The message displayed to the user when asking for input.
        validation_func (function): A function that return True if it's valid, otherwise False.              
        error_msg (str): The message displayed to the user when the input is invalid.
    Returns:
        str: The valid user input.
    """
    while True:
        user_input = input(input_msg)
        if validation_func(user_input):
            return user_input
        else:
            print(error_msg)

def main():

    logger=create_logger('User_Registration')
    
    first_name = valid_input(
        "Enter your first name: ",
        is_valid_name,
        "Invalid first name. It must start with an uppercase letter and be at least 3 characters long."
    )
    
    last_name = valid_input(
        "Enter your last name: ",
        is_valid_name,
        "Invalid last name. It must start with an uppercase letter and be at least 3 characters long."
    )
    
    email = valid_input(
        "Enter your email: ",
        is_valid_email,
        "Invalid email,Format for is 'deven123@gmail.com'."
    )
    
    mobile = valid_input(
        "Enter your mobile number (e.g., 91 9765859088): ",
        is_valid_mobile,
        "Invalid mobile number,Format for is 'XX XXXXXXXXXX'."
    )
    
    password = valid_input(
        "Enter your password: ",
        is_valid_password,
        "Invalid password. It must be at least 8 characters long"
    )
    
    logger.info(f"First Name: '{first_name}' - Valid")
    logger.info(f"Last Name: '{last_name}' - Valid")
    logger.info(f"Email: '{email}' - Valid")
    logger.info(f"Mobile: '{mobile}' - Valid")
    logger.info(f"Password: '{password}' - Valid")
    logger.info(f"User Successfully Registered")

if __name__ == "__main__":
    main()