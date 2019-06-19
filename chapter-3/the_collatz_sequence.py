'''
the_collatz_sequence.py
Author: Yashraj Kakkad
Chapter 3, Automate the Boring Stuff with Python
'''


def collatz(number):
    if not number % 2:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1


def main():
    print("Enter an integer: ")
    try:
        i = int(input())
    except ValueError:
        print("That's not an integer!")
        exit(0)
    while True:
        i = collatz(i)
        if i is 1:
            break


if __name__ == "__main__":
    main()
