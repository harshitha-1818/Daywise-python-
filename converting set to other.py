myset = {1,2,3}
#set to dict
mydict=dict.fromkeys(myset,0)#we cannot change directly set to the dict 
print(mydict)
#so,we use fromkeys function to convert the set to dict
'''set to list'''
my_list = list(myset)
print(my_list)
#set to tuple
mytuple= tuple(myset)
print(mytuple)