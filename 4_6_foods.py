my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('Shutki')
friend_foods.append('Paya')

print(my_foods)
print(friend_foods)
print("====================\n")


#First 3
for food_selection in my_foods[:3]:
    print(food_selection)
    print("====================\n")

#middle
for food_selection in my_foods[1:3]:
    print(food_selection)
    print("====================\n")


#last 3
for food_selection in my_foods[3:4]:
    print(food_selection)
    print("====================\n")


for looping in my_foods[:]:
    print(looping)
    print(", are one of my fav food")
    print("====================\n")
    print("====================\n")

for looping in my_foods[:]:
    print(looping)
    print(", one of my friend's fav food")
    print("====================\n")

