mylist = [2, 5, 2, 8, 5, 3, 2, 9, 6, 2, 6]
newlist = []


for i in mylist:
    if i not in newlist:
        newlist.append(i)


print(mylist)
print(newlist)
