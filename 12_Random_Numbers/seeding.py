import random

random.seed(1)
print("seed = 1: ", random.random())
print("seed = 1: ", random.randint(5,10))

random.seed(2)
print("seed = 2: ", random.random())
print("seed = 2: ", random.randint(5,10))

random.seed(1)
print("\nseed = 1: ", random.random())
print("seed = 1: ", random.randint(5,10))

random.seed(2)
print("seed = 2: ", random.random())
print("seed = 2: ", random.randint(5,10))