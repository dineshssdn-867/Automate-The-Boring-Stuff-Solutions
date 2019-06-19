'''
strong_password_detection.py
Author: Yashraj Kakkad
Chapter 7, Automate the Boring Stuff with Python
'''

import re


def strong_password(password):
    if(len(password) < 8):
        return False
    upperCaseRegex = re.compile(r'[A-Z]')
    if upperCaseRegex.search(password) == None:
        return False
    lowerCaseRegex = re.compile(r'[a-z]')
    if lowerCaseRegex.search(password) == None:
        return False
    digitRegex = re.compile(r'.*(\d).*')
    if digitRegex.search(password) == None:
        return False
    return True


def main():
    password = input("Enter a password: ")
    print("Strong") if strong_password(password) else print("Not strong")


if __name__ == "__main__":
    main()
