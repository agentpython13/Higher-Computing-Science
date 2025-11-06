'''
password = input('Enter your password:  ')
total = 0
for counter in range(0, len(password)):
    total += ord(password[counter])
check = total % 11
newPassword = password + str(check)
print(newPassword)

animal = input('Enter the name of an animal in lowercase:  ')
letter = animal[0]
newLetter = chr(ord(animal[0])-32)
newAnimal = newLetter + animal[1:]
print(newAnimal)
'''
special = ['$', '#', '%']
password = input('Please enter your password:  ')
while ord(password[0]) < 65 or ord(password[0]) > 90:
    print('Your password is not secure! Please make the first character a captital letter.')
    password = input('Please enter your password: ')
while password[len(password)-1] not in special:
    print('Your password is not secure! Please make the last character either "$", "%" or "#"')
    password = input('Please enter your password: ')


