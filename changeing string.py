name = 'harsha'
age = 19
formatted_str_1 =f"my name is {name} and  i am {age} years odd"
print(formatted_str_1)
formatted_str_2 = "my name is {} and  i am {} years old".format(name,age)
print(formatted_str_2)
formatted_str_3 = "my name is %s and  i am %d years old" %(name,age)
print(formatted_str_3)
formatted_str_4 = "my name is {0} and  i am {1} years old".format("harshitha",18)
print(formatted_str_4)
formatted_str_5 = "my name is {name} and  i am {age} years old".format(name="harshi",age=18)
print(formatted_str_5)