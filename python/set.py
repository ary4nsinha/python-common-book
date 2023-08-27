# set = collection which is unordered, unindexed. no duplicate values 

utensils = {"bowl", "fork", "knife", "knife"}
dishes = {"cup", "plate", "pot","knife"}
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))

#for x in dinner_table:
    #print(x) #order is not exact like we gave. set is faster than a list if you wanna check whats in the set 
#they dont have duplicates only one knife will show 