'syntax error is typo error'

#1 SyntaxError
# a = 5 print(a)
'SyntaxError: invalid syntax'
a = 5 
print(a)


#2 SyntaxError
# print(a))
"SyntaxError: unmatched ')'"
print(a)

#3 type Error
# a = a + '10' 
"TypeError: unsupported operand type(s) for +: 'int' and 'str'"


#4 import Error
# import xyz
"ModuleNotFoundError: No module named 'xyz'"


# 5 name error 
# b = c 
"NameError: name 'c' is not defined"


# 6 file not found 
# f = open('new_file.txt')
"FileNotFoundError: [Errno 2] No such file or directory: 'new_file.txt'"


# 7 value error 
num = [1, 3, 5]
num.remove(1)
print(num)
# num.remove(7) 
'ValueError: list.remove(x): x not in list'


# 8 index error 
get1 = num[0]
print(get1)
# get2 = num[3] 
'IndexError: list index out of range'

# 9 key error 
person = {'name': 'Thomas'}
# person['age']
"KeyError: 'age'"
print(person['name'])
