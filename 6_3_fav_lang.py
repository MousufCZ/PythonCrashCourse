fav_lang = {
    'jen': 'python',
    'dum': 'c',
    'barthamalous': 'ruby',
    'purgunal': 'python',
    }

#print("Dum's fav language is :" +
 #     fav_lang['dum'].title() +
 #     ".")


for name, language in fav_lang.items():
    print(name.title() + "'s fav lang is " +
          language.title() + ".")


print("\n===========================================\n")
print("Focus on key\n")

for name in fav_lang.keys():
    print(name.title())


print("\n===========================================\n")
print("Special message with in the name list in dictionary\n")


friends = ['jen', 'purgunal']
for name in fav_lang.keys():
    print(name.title())


    if name in friends:
        print("\n Hi" + name.title() + ", I see your fav programming lang is " +
        fav_lang[name].title() + "!")


print("\n===========================================\n")
print("Not in the dictionary\n")


if 'Mousuf' not in fav_lang.keys():
    print("Mousuf, please tell us your fav language")
    


print("\n===========================================\n")
print("Looping through to sort out name\n")

for name in sorted(fav_lang.keys()):
    print(name.title() + ", thank you for taking the poll.")
    

print("\n===========================================\n")
print("focus on value\n")

print("The languages that have been mentioned are: ")
for language in fav_lang.values(): # Value
    print(language.title())
    

print("\n===========================================\n")
print("All values in the Set\n")

for language in set(fav_lang.values()): # Value
    print(language.title())

