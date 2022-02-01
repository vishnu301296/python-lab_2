
a = [1,2,3,4,5,6,7,8]

b = []

for x in range (len(a)+1):
    for y in range(x):

        b.append(a[y:x])
 

print(b)