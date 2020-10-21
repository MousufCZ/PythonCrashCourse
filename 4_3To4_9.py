#4-3 : Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive

count_to_twenty = range(1,21)
#for count in count_to_twenty:
    #print (count)

#for count_to_twenty2 in range(1,21):
    #print (count_to_twenty2)


#4-4. One Million:
million = list(range(1, 1000001))
#for mill_print in million:
    #print(mill_print)


#4-5. Summing a Million:
#print (min(million))
#print (max(million))


#4-6. Odd Numbers
odd_number = list(range(1,20,2))
#print (odd_number)


#4-7. Threes
#threes = []
#for multiple in range(1,11):
    #threes.append(multiple*3)
#print (threes)

threes = [values * 3 for values in range (1,11)]
#print (threes)


#4-8. Cubes: A number raised to the third power is called a cube For example, the cube of 2 is written as 2**3 in Python Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube
#integers = range(1, 11)
#for cube in integers:
    #print ("This is a cube: ")
    #print(cube ** 3)


integers = list(range(1, 11))
for cube in integers:
    print ("This is a cube: ")
    print(cube ** 3)

