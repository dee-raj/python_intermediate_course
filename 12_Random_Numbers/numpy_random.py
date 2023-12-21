import numpy as np 

#  1D array 
arr = np.random.rand(5)
'Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).'
print("Array using numpy with random: ", arr)

# 2D array 
arr_2d = np.random.rand(2,2)
print("2D array using numpy with random: \n", arr_2d)

# for n_d array just give second args as n in np.random.rand(x, n)


# random integer with a size
rand_arr = np.random.randint(3, 15, 4)
print("Random int with a size: ", rand_arr)


# arrry of higher dimension containing int values 
I3 = np.random.randint(1, 10, (3,3))
print("\n\n3x3 array:\n",I3) 


# To shuffle a array
my_arr = np.array([[1, 3, 5], [0, 2, 4], [7, 8, 9]])
print(f"\nOriginal array:\n{my_arr}")
print()
np.random.shuffle(my_arr)
print(f"Shuffle array:\n{my_arr}")



print("\n numpy seed")
np.random.seed(1)
print(np.random.rand(3,4))

np.random.seed(1)
print()
print(np.random.rand(3,4))