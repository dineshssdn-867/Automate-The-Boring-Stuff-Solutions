'''
add_to_inventory.py
Author: Yashraj Kakkad
Chapter 5, Automate the Boring Stuff with Python
'''


def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


def display_inventory(inventory):
    count = 0
    for k, v in inventory.items():
        print(v, k)
        count += v
    print("Total number of items:", count)


def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)


if __name__ == "__main__":
    main()
