#Admission for anyone under age 4 is free.
#Admission for anyone between the ages of 4 and 18 is $5.
#Admission for anyone age 18 or older is $10.

#age = 70
#if age < 4:
#    print("Your admission cost is £0.")
#elif age < 18:
#    print("Your admission cost is £5.")
#elif age < 65:
#    print("Your admission cost is £10.")
#else:
#    print("You are too old!! Your life experience is too amazing to wait in the queue... we are shutting down the park so you and your pals can have the whole place to yourself.")


age = 70

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    prine = 10
#else:          #Don't need to have else in Py
elif age > 65:
    price = 0
print("Your admission cost is £" + str(price) + ".\n")
