#String to List
my_str = "Does it make any sense ?"
str_list = my_str.split()
'default sep=" "'
print("without separator: ",str_list)

ask = "Does it make any sense ?how are you ?"
my_list = ask.split('?')
'Return a list of the substrings in the string, using sep as the separator string.'
print("with separator: ",my_list)
print("length: ",len(my_list))

my_num = '1; 2; 3; 4; 5; 6; 7;'
num_list = my_num.split(';',3)
print("check only 3 seperator: ", num_list)
print("length: ",len(num_list))


# List to String
new_string = ' '.join(str_list)
print(f"\nstr_list: {str_list} \ttype: {type(str_list)}")
print(f"New string: {new_string}\t type: {type(new_string)}")