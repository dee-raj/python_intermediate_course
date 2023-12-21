import random

# for random float numbers 
ran_f = random.random()
'random() -> x in the interval [0, 1).'
print("Random float num 0 to 1: ", ran_f)

rand_10 = random.uniform(1, 10)
'Get a random number in the range [a, b) or [a, b] depending on rounding.'
print("random num in a range: ", rand_10)


#for random integer 
rand_int = random.randint(2,11)
'Return random integer in range [a, b], including both end points.'
print("\nRandom integer: ", rand_int)

rand_num = random.randrange(1, 20, 2)
'Choose a random item from range(start, stop[, step]).'
print("Random range: ", rand_num)


ran_norm = random.normalvariate(2, 4)
'''Normal distribution.
mu is the mean, and sigma is the standard deviation.'''
print("Random variate: ", ran_norm)
