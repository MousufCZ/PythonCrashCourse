promt = "\nEnter your fav city: "
promt += "\nEnter 'quit' to end the program."


print("\n=================================")
print("======== Using Break")
print("=================================\n\n")

while True:
    city = input(promt)

    if city == 'quit':
        break
    else:
        print("I'd love to fo to " + city.title() + "!")

# 126 126 126 126
