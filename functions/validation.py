import re
import datetime

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


def valid_date(date):
    try:
        date = datetime.datetime.strptime(date, '%d-%m-%Y')
        min_date = datetime.datetime.strptime('01-01-1920', '%d-%m-%Y')
        max_date = datetime.datetime.now()
        if date < min_date or date > max_date:
            return False
        return True
    except ValueError:
        return False

# check if essential data is valid or not while creating user


def invalid_signup(data):
    if "email" not in data:
        return "Email is required", True
    elif not valid_email(data["email"]):
        return "Invalid Email", True
    elif "password" not in data:
        return "Password is required", True
    elif not valid_password(data["password"]):
        return "Password must contain upper case letter, lower case letter, number and a special character", True
    elif "name" not in data:
        return "Name is required", True
    elif not valid_name(data["name"]):
        return "Invalid Name", True
    elif "surname" not in data:
        return "Surname is required", True
    elif not valid_name(data["surname"]):
        return "Invalid Surname", True
    elif "gender" not in data:
        return "Gender is required", True
    elif data["gender"] not in ["M", "F", "O"]:
        return "Gender must be one of 'M' for male, 'F' for female or 'O' for other", True
    elif "birthDate" not in data:
        return "Birth Date is required", True
    elif not valid_date(data["birthDate"]):
        return "Invalid Birth Date", True
    else:
        return "", False
