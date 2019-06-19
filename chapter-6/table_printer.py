'''
table_printer.py
Author: Yashraj Kakkad
Chapter 6, Automate the Boring Stuff with Python
'''


def print_table(tableData):
    colWidths = [0] * len(tableData)
    for i, l in enumerate(tableData):
        for word in l:
            colWidths[i] = max(colWidths[i], len(word))
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=" ")
        print()


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    print_table(tableData)


if __name__ == "__main__":
    main()
