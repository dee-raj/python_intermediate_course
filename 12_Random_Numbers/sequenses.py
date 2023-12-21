import random
mylist = list(["one", "two", "three", "four", "five"])
print(mylist)

# picking a random element
a = random.choice(mylist)
print(f"A random element from mylist: {a}")

# picking group of elements at a time 
grp3 = random.sample(mylist, 3)
print("Group of 3: {}".format(grp3))


# picking group of elements but they may same
my_choices = random.choices(mylist, k=3)
print("\nRandom Choices: ", my_choices)



# to shuffle the list element
random.shuffle(mylist)
'Shuffle list x in place, and return None.'
print("Shuffled list:", mylist)