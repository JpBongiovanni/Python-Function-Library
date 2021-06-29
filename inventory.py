from collections import Counter

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':12}

print(inv)

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total = item_total + v

    print("Total number of items:" + str(item_total))

displayInventory(inv)

def addToInventory(inventory, addedItems):
    #Code goes here
    for l in addedItems:
        if l is not inventory:
            inventory[l]=1
        if l is inventory:
            # print(l.count)
            inventory[l] = inventory[l]+1


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)

print(inv)
# inv = addToInventory(inv, dragonLoot)

# displayInventory(inv)