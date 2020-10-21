square = [value**2 for value in range (1,11)]
print (square)


#--------------------
sq = []
for value in range (1,11):
    sq.append(value**2)  #We refractored sq equation in to the append

#print (sq)
    
#--------------------
#CODE REFRACTORED
sq = []
for value in range (1,11):
    square = value **2
    sq.append(square)

#print (sq)

#--------------------
digits = list (range(0,6))
#print (min(digits))
#print (max(digits))
#print (sum(digits))

