promt = "\nTell me something, and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program."

message = " "
while message != 'quit':
    message = input(promt)
    #print(message)

    #if message != 'quit':
       # print(message)

print("\n=================================")
print("=================================")
print("=================================\n\n")

active = True
while active:
    message = input(promt)

    if message == 'quit':
        active = False
    else:
        print(message)