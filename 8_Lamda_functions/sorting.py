points2D = [(1, 2), (15, 3), (4, -3), (-7, 0)]

# sort by default
points2D_sorted = sorted(points2D)

print("original: ",points2D)
print("default sorted: ",points2D_sorted)

#sort by lambda key
points2D_sorted_key = sorted(points2D, key=lambda x: x[1])
print("sorting with lambda: ", points2D_sorted_key)



def sort_by_sum(x):
   return x[1] + x[0]
points2D_sorted_y = sorted(points2D, key=sort_by_sum)
print("\nsorting with sum & def: ", points2D_sorted_y)

points2D_sorted_y = sorted(points2D, key=lambda x: x[0] + x[1])
print("sorting with sum & lambda: ", points2D_sorted_y)
