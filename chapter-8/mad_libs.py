'''
madlibs.py
Author: Yashraj Kakkad
Chapter 8, Automate the Boring Stuff with Python
'''
import re

fileName = input(
    "Enter file name to read from: (Press enter if you want to use sample.txt)")
if fileName == "":
    fileName = "sample.txt"
fileObject = open(fileName)
fileContent = fileObject.read()
fileObject.close()
madlibsRegex = re.compile('NOUN|ADJECTIVE|VERB|ADVERB')
matches = madlibsRegex.findall(fileContent)

for match in matches:
    replace = input('Enter a ' + match + ': ')
    fileContent = fileContent.replace(match, replace, 1)

print(fileContent)
fileObject = open(fileName, "w")
fileObject.write(fileContent)
print("File updated successfully!")
