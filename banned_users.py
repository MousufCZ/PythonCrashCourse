banned_u = ['Ice tea', 'rick', 'alphabetriam']
user = 'Ice tea'
#user = 'maria'

if user not in banned_u:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + ", you have been banned. Please contact administrator")
