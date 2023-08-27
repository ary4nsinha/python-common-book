# it is a changeable, unordered collection of unique key value pairs
# they are fast because they use hashing, allow us to access a value quickly 

capitals = {'USA':'Washington DC','India':'New Delhi', 'China':'Bejing','Russia':'Moscow'}

#capitals.update({'Gemrany':'Berlin'})
capitals.update({'USA':'Ohio'})
capitals.pop('China')

for key,value in capitals.items():
    print(key,value)

#print(capitals['India'])
#print(capitals.keys())