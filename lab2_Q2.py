string = input("enter any sentence  :")

count = {}

for x in string:

    if x in count:
        count[x] += 1
    else:
        count[x] = 1

print("the count of characters in  frequency are : \n",str(count))