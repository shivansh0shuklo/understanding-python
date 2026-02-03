#Q the inventory manager (dictionary,printing)

inventory = {'apples': 50,'bananas': 20,'oranges': 15}

inventory['apples']+=10
inventory['oranges']+=5
print(inventory)
inventory['bananas']-=inventory['bananas']
print(inventory)
for item,value in inventory.items():
    print('Item:',item,'| quantity: ',value)