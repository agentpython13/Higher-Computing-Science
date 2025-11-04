password = input('Enter your password:  ')
total = 0
for counter in range(0, len(password)):
    total += ord(password[counter])
check = total % 11
newPassword = password + str(check)
print(newPassword)
                
