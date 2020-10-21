# A list that cannot be changed
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
print("==================\n")

#dimensions[0] = 250 

original_dimensions = dimensions
print("Original Dimensions")
for dimension in dimensions:
    print(dimension)


dimensions = (400, 100)
print ("\nModified Dimensions\n")
for dimension in dimensions:
    print(dimension)
