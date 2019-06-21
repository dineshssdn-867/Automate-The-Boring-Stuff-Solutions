import re
import os

regex = input("Enter regex: ")
searchRe = re.compile(regex)
folder = input("Enter folder: ")
txtRe = re.compile(r'.txt$')

for file in os.listdir(folder):
    # Proceed for only txt files
    if txtRe.search(file) is not None:
        fileObj = open(os.path.join(folder, file))
        fileContent = fileObj.readlines()
        # Read file content line by line
        for line in fileContent:
            # Print the line having some match for the regular expression
            if searchRe.search(line) is not None:
                print(line)
