'''
comma_code.py
Author: Yashraj Kakkad
Chapter 4, Automate the Boring Stuff with Python
'''


def comma_code(items):
    item_len = len(items)
    if item_len == 0:
        return ""
    elif item_len == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

    # Naive, brute force approach:-
    # item_string = ""
    # for i, item in enumerate(items):
    #     if(len(items) > 1):
    #         if i == len(items) - 2:
    #             item_string += str(item) + " and "
    #             # item_string = item_string[:len(item_string)-2] + " and " + str(item)
    #         elif i == len(items) - 1:
    #             item_string += str(item)
    #         else:
    #             item_string += str(item) + ", "
    #     elif(len(items) == 1):
    #         return str(items[0])
    #     else:
    #         return ""
    # return item_string


def main():
    print(comma_code(['one', 'two', 'three', 'four']))
    print(comma_code(['one', 'two']))
    print(comma_code(['justone']))
    print(comma_code([]))


if __name__ == "__main__":
    main()
