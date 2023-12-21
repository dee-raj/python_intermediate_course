import secrets 

a = secrets.randbelow(20)
"Return a random int in the range [0, n)."
print("Secret Random int: ",a)


# 4 = max 1111
b = secrets.randbits(4)
'getrandbits(k) -> x. Generates an int with k random bits.'
print("random int with 4 bits: ", b)


my_list = list(["one", "two", "three", "four", "five"])
print("\nMy list: ", my_list)

val = secrets.choice(my_list)
print("secret choice: ", val)