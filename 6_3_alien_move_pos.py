alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print("Original x-pos: " + str(alien_0['x_pos']))

#change speed
alien_0['speed'] = 'fast'

#Moving alien to the right
# Determine how far to move based on the speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #the fast alien
    x_increment = 3

# The new pos is the old pos plus the increment
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print("The new x-pos: " + str(alien_0['x_pos']))

