setX = {2,3,4,5,6,7,8}
print("orginal set:",setX)

# setY = setX  # it wiil modify the original set even updating copied one
setY = setX.copy() # Return a shallow copy of a set.
print("copy set:",setY)

setY.add(0)
print("after adding 0 copy set:",setY)
print("after adding 0 orginal set:",setX)