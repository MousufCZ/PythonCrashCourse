"""Print a simple greeting to each user in the list."""
print("##########################################")
print("###### - Passing a List")
print("##########################################\n")


def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['a', 'b', 'c', 'd']

greet_users(usernames)
