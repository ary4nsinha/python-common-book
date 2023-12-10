myList = [10,20,30,40,50]

newList = myList[:]
print(newList)

aliasList = myList
aliasList.append(60)
print(myList)