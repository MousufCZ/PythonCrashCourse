#Make an empty list for storing aliens
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow'}
    aliens.append(new_alien)




# Change characteristics
for alien in aliens[0:6]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[6:8]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 115


# Show the firt 5 aliens
for alien in aliens[:31]:
    print(alien)
print("...")

#Show the number of aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
