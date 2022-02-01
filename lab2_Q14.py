user_1 = int(input("How many items need : "))

items = list()

for x in range (user_1):
    items.append(input("enter your items : "))

print(items)

# To remove a item from list

user_2 = input("Enter  the items to be removed : ")

if user_2 in items:
    items.remove(user_2)

    print(items)   

else:
    print("No items founded")