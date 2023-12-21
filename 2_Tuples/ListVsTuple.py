# space complexity
import sys
mylist = [0, 1.23, "Hello", True, b'dee']
mytuple = (0, 1.23, "Hello", True, b'dee')

list_size = sys.getsizeof(mylist)
tuple_size = sys.getsizeof(mytuple)

print(f"{list_size} bytes")
print(f"{tuple_size}  bytes")



# time complexity
import timeit
list_time = timeit.timeit(stmt="[1, 2, 3, 5, 7, 11, 13, 17, 19]", number=100000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 5, 7, 11, 13, 17, 19)", number=100000)

print(list_time)
print(tuple_time)