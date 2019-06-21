'''
multiclipboard.py
Author: Yashraj Kakkad
Chapter 8, Automate the Boring Stuff with Python
'''
import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
        print("Deleted successfully!")
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        print("Here we go: ")
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print("Deleted everything")
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print("Copied successfully")
    else:
        print("Invalid command/key not found")

mcbShelf.close()
