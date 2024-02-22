# x = "dog"
# y = "cat"

# # a. x + y
# print(f"a. {x} + {y} = {x + y}")  # Output: dogcat

# # b. "the " + x + " chases the " + y
# print(f"b. {'the ' + x + ' chases the ' + y} = {'the ' + x + ' chases the ' + y}")  # Output: the dog chases the cat

# # c. x * 4
# print(f"c. {x} * 4 = {x * 4}")  # Output: dogdogdogdog
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_numbers = [num for num in list1 if num in list2]

# common_numbers = [num for num in list1 if num in list2]

# print("Common numbers:", common_numbers)
dic = {'name':'vinayak','age':20}
print(dic.values())
dic.clear()
print(dic)
my_set2 = {'banana','apple','orange','pazham'}
my_set = {'banana','apple','orange'}
print('banana' in my_set)
my_set.add('green apple')
print(my_set)
my_set.update(['fruit','beans'])
print(my_set.difference(my_set2))