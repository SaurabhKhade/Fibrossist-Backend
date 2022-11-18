import re

# email validation regex 
email_validation = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# strong password validation regex 
password_validation = r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$'
# name validation regex 
name_validation = r'[A-Za-z]{2,25}'

def valid_email(email):
    if re.fullmatch(email_validation, email):
        return True
    else:
        return False

def valid_password(password):
    if re.fullmatch(password_validation, password):
        return True
    else:
        return False

def valid_name(name):
    if re.fullmatch(name_validation, name):
        return True
    else:
        return False

# check if essential data is valid or not while creating user
def invalid_signup(data):
    if "email" not in data:
        return "Email is required"
    elif not valid_email(data["email"]):
        return "Invalid Email"
    elif "password" not in data:
        return "Password is required"
    elif not valid_password(data["password"]):
        return "Password must contain upper case letter, lower case letter, number and a special character"
    elif "name" not in data:
        return "Name is required"
    elif not valid_name(data["name"]):
        return "Invalid Name"
    elif "surname" not in data:
        return "Surname is required"
    elif not valid_name(data["surname"]):
        return "Invalid Surname"
    elif "age" not in data:
        return "Age is required"
    elif "gender" not in data:
        return "Gender is required"
    elif data["gender"] not in ["M","F","O"]:
        return "Gender must be one of 'M' for male, 'F' for female or 'O' for other"
    else:
        try:
            int(data["age"])
            return False
        except:
            return "Age must be a number"

# def invalid_signin(data):
#     if "email" not in data:
#         return "Email is required"
#     elif "password" not in data:
#         return "Password is required"
#     else:
#         return False