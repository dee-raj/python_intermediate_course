
# Warnings do not get confusied

# = +
def foo(a_list):
   a_list = a_list + [0, 1, 3, 4]

b_list=[4, 5, 6]
foo(b_list)
print(b_list)


# +=
print()
def foo(a_list):
   a_list += [0, 1, 3, 4]

b_list=[4, 5, 6]
foo(b_list)
print(b_list)

