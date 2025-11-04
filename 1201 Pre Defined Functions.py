'''
password = input('Enter your password:  ')
total = 0
for counter in range(0, len(password)):
    total += ord(password[counter])
check = total % 11
newPassword = password + str(check)
print(newPassword)
'''
animal = input('Enter the name of an animal in lowercase:  ')
letter = animal[0]
newLetter = chr(ord(animal[0])-32)
newAnimal = newLetter + animal[1:]
print(newAnimal)


