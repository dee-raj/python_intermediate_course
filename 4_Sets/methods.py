new_set = set() #empty 
new_set.add(2)
new_set.add(0)
new_set.add(4)
new_set.add(6)
new_set.add(3)
print(new_set)

new_set.remove(0) #Remove an element from a set; it must be a member
print("after removed 3",new_set)

new_set.discard(5) #Remove an element from a set if it is a member.
print(new_set)

item = new_set.pop() # returns poped item
print("poped element: ", item)
print(new_set)


print("\n\n===========xxxxxxxxxxxxxx============xxxxxxxxxxx=============xxxxxxxxxxxx===================xxxxxxx=========")
setA = {1,2,3,4,5,6,7}
setB = {3,4,7,2}
print(f"A = {setA}\t B = {setB}")

# Report whether another set contains this set
AcB = setA.issubset(setB)
print("\nis A subset Of B:", AcB)
BcA = setB.issubset(setA)
print("is B subset Of A:", BcA)

# Report whether this set contains another set.
AcB = setA.issuperset(setB)
print("\nis A superset Of B:", AcB)
BcA = setB.issuperset(setA)
print("is B superset Of A:", BcA)


setC = {1,5,6,8}
# Return True if two sets have a null intersection.
dissBC = setB.isdisjoint(setC)
print("are B and C disjoint set:",dissBC)

dissAC = setC.isdisjoint(setA)
print("are B and C disjoint set:",dissAC)