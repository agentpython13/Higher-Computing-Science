#modular programming
"""
def displayNames(nameList):
  print("Current list")
  for loop in range(len(nameList)):
    print("Forename",nameList[loop][0])
    print("Surname",nameList[loop][1])

nameList = [["Matthew","Reid"]]
numNames = int(input("How many names do you wish to add?"))
for names in range(numNames):
  newForename = str(input("Please enter a forename"))
  newSurname = str(input("Please enter a surname"))
  nameList.append([newForename, newSurname])

displayNames(nameList)

# Predict and Run - Task 2

def displayScoreData(scores):
  average = sum(scores)/len(scores)
  print("Average score:",round(average,1))
  print("Scores ranged from:")
  print(min(scores),"to",max(scores))

# Main program
scores = [4,6,8,5,6,3,5,9,10,2,4,6,3,5]
displayScoreData(scores)
scores = [50,51,52,56,59,68]
displayScoreData(scores)

"""
'''
def module1(first, second, third):
  volume = first * second * third
  print("Volume =",volume)

def module2(monday):
  monday = monday/10
  return monday

def module3(blue, red):
    total = 0
    for counter in range(blue, red):
        total = total + 2
        print(total)
        return total

def module4(up, down):
  middle = up % down
  top = int(up/down)
  total = middle + top
  return total

num1 = 100
num2 = 6
num3 = 9
print(module2(num1) + module3(num2, num3))
'''
