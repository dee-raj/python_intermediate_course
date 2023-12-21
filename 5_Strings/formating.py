'''
There are 3 way of formating string
   %
   .format()
   f-string
'''
# 1) using %
print("using %")
var = "cream"
my_fav = "ice %s" %var
'for str %s'
print(my_fav)

var = 7
my_fav = "CR%d" %var
'for int value %d'
print(my_fav)

var = 3.14
pi = "pi= %f" %var
'floating point %.6f here 6 is digit after .'
print(pi)



# 2) .format()
print("\nusing .format()")
new = 18
my_str = "King {}".format(new)
print(my_str)

price = 219.290
cost = "Rs {:.2f}".format(price)
print(cost)

a= 34
b= 75
diff = "{} - {} = {}" .format(b, a, b-a)
print(diff) 



# 3) f-string
print("\nusing f-string")
cap = "Dhoni"
hero = f"Cricket king {cap}"
print(hero)

num = 7
channel = f"Chess{num}Dee" 
print(channel)

seat = 1040
code = 361
center = 'vasai'
venue = f"Seat: {seat} \tcode: {code} \tcenter: {center}"
print(venue)