players = ['charlies', 'martina', 'michael', 'florance', 'eli']
print (players[0:3])
print (players[-3])
print ("================ \n")


print("Here are the first 3 players on my team: ")
for player in players[:]:
    print(player.title())
print ("================ \n")


players_copy = players[:]

players.append('Mousuf')
players_copy.append('Wallid')

print("My frind's choices :")
print(players_copy)
