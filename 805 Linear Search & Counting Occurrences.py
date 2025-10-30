'''
names = ['Jim', 'James', 'Jan', 'Jimmy', 'John', 'Jenna', 'Jonny' ]
counter = 0
nameToFind = 'John'
found = False
foundPosition = -1
while counter < len(names) and found == False:
  if names[counter] == nameToFind:
    found = True
    foundPosition = counter
  else:
    counter = counter + 1

if found == True:
  print (nameToFind, " was found at position: ", foundPosition)
else:
  print (nameToFind, " wasn't found. Too bad.")'

teams = ["Man Utd", "Man City", "Spurs", "Liverpool", "Chelsea", "Arsenal", "Newcastle"]
goalsScored = [63, 89, 65, 79, 59, 69, 35 ]

occurrences = 0
#Loop through every team
for i in range(len(teams)):
  if goalsScored[i] < 60:
    occurrences = occurrences + 1
    print (teams[i] +  " scored more than 60 goals")

#once the loop has finished, print the total number of teams that has scored more than 60
print (str(occurrences) + " teams have scored more than 60")
'''

'''
# 805Task3.py
# Standard Algorithms - Linear Search & Counting Occurrences

# Investigate and modify

def getTargetCharacter():
  target = input("Enter the character you are looking for")

  return target

def getCharacters():
  characters = ["Desperate Dan", "Numbskulls", "Dennis the Menace", "Minnie the Minx", "Walter", "Gnasher", "Billy Whizz"]

  return characters

def findCharacterPosition(oneToFind):
  found = False
  foundPosition = -1
  for i in range(len(characters)):
    if characters[i] == oneToFind:
      found = True
      foundPosition = i

  if found == False:
    print("The character was not found.")
  else:
    print("The character was found at position:", foundPosition)

  return foundPosition

#. *************MAIN*************

target = getTargetCharacter()
characters = getCharacters()
foundPosition = findCharacterPosition(target)
'''
# 805Task4.py
# Standard Algorithms - Linear Search & Counting Occurrences

# Investigate and modify

def getTarget():
  targetAnimal = input("Please enter the target animal you are searching for")

  return targetAnimal

def getCircusAnimalsList():
  animals = ["giraffe", "chicken", "lion", "cheetah", "rat", "elephant", "snake", "chicken", "horse"]

  return animals

def countOccurrences(targetAnimal, animals):
  occurrences = 0
  for i in range(len(animals)):
    if animals[i] == targetAnimal:
      occurrences += 1
  return occurrences
  #for i in range(len.....):
  #  if animals[i] == ......:
  # FINISH OFF THIS CODE

def printOccurrences(occurrences):
  print(occurrences)


#*************  MAIN *************

targetAnimal = getTarget()
animals= getCircusAnimalsList()
occurrences = countOccurrences(targetAnimal, animals)
printOccurrences(occurrences)