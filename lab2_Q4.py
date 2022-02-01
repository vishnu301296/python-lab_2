from collections import Counter


string =input ("enter any sentence  :")

user_len = Counter(string)

for x,y in user_len.items():


    if y > 1:
   
     print("{0} repeat at {1} times".format(x,y))
