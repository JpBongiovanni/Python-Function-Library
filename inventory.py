from collections import Counter

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total = item_total + v

    print("Total number of items:" + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    #Code goes here
    for l in addedItems:
        inventory.setdefault(l, 0)
        inventory[l] += 1
    return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(stuff, dragonLoot)

displayInventory(inv)
# inv = addToInventory(inv, dragonLoot)

# displayInventory(inv)