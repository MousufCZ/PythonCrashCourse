#alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])

#new_points = alien_0['points']
#print("You just earned " + str(new_points) + " points!")

#del alien_0['points']
#print(alien_0)



#print(alien_0)

#alien_0['x_pos'] = 0
#alien_0['y_pos'] = 25
#print(alien_0)


print("\n==============================")
print("===== Nesting =======")
print("==============================\n")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
