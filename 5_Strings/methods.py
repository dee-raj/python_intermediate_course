string = "        Hello World             "
orinal_len = len(string)
print("original: ",string)
print("original length: ", orinal_len)


# remove white space 
my_string = string.strip()
'Return a copy of the string with leading and trailing whitespace removed.'
new_len = len(my_string)
print("strip: ",my_string)
print("new length: ", new_len)

# ==========================xxxxxxxxxxxxxxxxxxx=========================xxxxxxxxxxxxxxxxxxxxxx=========================
# convert to UPPERCASE
upper_str = my_string.upper()
'Return a copy of the string with upper case'
print("\nupper: ", upper_str)


# convert to lowercase
lower_str = my_string.lower()
'Return a copy of the string with lower case'
print("lower: ", lower_str)



# ===============================xxxxxxxxxxxxx==================xxxxxxxxxxxxxxxxxx=================xxxxxxxxxxxxxx====================
# check sub-strings
is_start_with = my_string.startswith('Hello')
'check if str is start with Hello'
print("\nis start with: ",is_start_with)

is_end_with = my_string.endswith('d')
'check if str is end with d'
print("is end with: ",is_end_with)



# ===========================xxxxxxxxxxxxxxxxx=================xxxxxxxxxxxxxxxxx=================xxxxxxxxxxxxxxx==============
#find index of char or sub-string
find_d = my_string.find('d')
'Returns index (int) if the str present in it else -1'
print("\nidx of d: ", find_d)

find_p = my_string.find('p')
print("idx of p: ", find_p)


find_w = my_string.find('World')
print("idx of world: ", find_w)



# ===============xxxxxxxxxxxx===================xxxxxxxxxxx====================xxxxxxxxxxxxxxxxx====================xxxxxxxxxxxxx=========
# count
counting_l = my_string.count('l')
'Returns no of char present in str'
print("\nNo of l: ",counting_l)

counting_a = my_string.count('a')
'Returns no of char present in str'
print("No of a: ",counting_a)



# ==================================xxxxxxxxxxxxxxxxxx===============================xxxxxxxxxxxxxxxxxxxxxx==========================
#replace 
new_str = my_string.replace('Hello', 'Hey')
'Try replace new if old exist'
print("\nreplaced str: ",new_str)

# n_str = new_str.replace('Hey', 'Hi')
n_str = my_string.replace('Hey', 'Hi')
print("if replace: ",n_str)