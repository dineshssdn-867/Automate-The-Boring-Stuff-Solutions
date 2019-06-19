'''
character_picture_grid.py
Author: Yashraj Kakkad
Chapter 4, Automate the Boring Stuff with Python
'''


def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            print(grid[-(i+1)][j], end='')
        print()


if __name__ == "__main__":
    main()

# Program Output:
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
