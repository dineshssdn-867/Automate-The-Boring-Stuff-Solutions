'''
regex_strip.py
Author: Yashraj Kakkad
Chapter 7, Automate the Boring Stuff with Python
'''

import re


def regex_strip(string, chars=""):
    stripRegex = None
    if chars == "":
        stripRegex = re.compile(r'\S+.*\S+')
        stripMatch = stripRegex.search(string)
        new_string = stripMatch.group(0)
        # new_string = stripRegex.sub('', string)
    else:
        stripRegex = re.compile(chars + r'(.*)' + chars)
        stripMatch = stripRegex.search(string)
        new_string = stripMatch.group(1)
        # print(len(new_string))
        # new_string = stripRegex.sub('', string)
    return new_string


def main():
    string = input("Enter a string: ")
    chars = input(
        "Enter the string to strip. Press enter to remove white-spaces: ")
    print(regex_strip(string, chars))


if __name__ == "__main__":
    main()
