"""
set: unordered, mutable, no duplication
"""
pieces = {"King", "Queen", "Rook", "Knight", "Bishop", "Pawn", "Rook"}
print("chess pieces: ",pieces)


"""
set() -> new empty set object 
set(iterable) -> new set object Build an unordered collection of unique elements.
"""

# with set function that takes an iterable item
odd_number = set([1, 3, 5, 7, 9, 11])
print(f"set of odd numbers: {odd_number}")

myset = set("Hello, there!")
print("My set:", myset)



new_set = set() #empty 
# new_set.add([2,4,6,8,0]) #list not valid
new_set.add(230.21)
new_set.add((2,7))
new_set.add(("one", "three"))
new_set.add("five")
print(f"\nNew set: {new_set}")