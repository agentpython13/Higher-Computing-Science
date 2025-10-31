'''
# 1001Task3.py
# Standard Algorithms - Finding Min + Max

# Investigate and modify

runner_name = ["AS","CM","ZN","OR","FP"]
runner_num = [2191,1789,1046,3391,2192]
runner_time = [49.18,51.36,42.58,58.59,64.03]
money_raised = [312.50,240.75,210.00,278.90,180.00]

def displayNumbers (numbers):
  for x in range(len(numbers)):
    print  (numbers[x]," ",end="")
  return

def findingMin (numbers):
  position = 0
  minimum = numbers[0]
  for index in range(1,len(numbers)):
    if numbers[index]<minimum:
      minimum = numbers[index]
      position = index
  print()
  print("The lowest number (minimum) in the list is",minimum,".")
  return position

displayNumbers(runner_time)
position = findingMin(runner_time)
print("The runner who was fastest is:",runner_name[position])
print("Their runner number was",runner_num[position])
print("The amount raised for charity was",money_raised[position])
'''
# 1001Task6.py
# Standard Algorithms - Finding Min + Max

# Investigate and modify

from random import *

numbers = []

def random20numbers():
  for x in range(20):
    numbers.append(randrange(1,51))
  return numbers

def displayNumbers (numbers):
  for x in range(20):
    print  (numbers[x]," ",end="")

def findingMax(numbers):
  maximum = numbers[0]
  for index in range(1,len(numbers)):
    if numbers[index]>maximum:
      maximum = numbers[index]
      
  print()
  print("The highest number (maximum) in the list is",maximum,".")

numbers = random20numbers()
displayNumbers(numbers)
findingMax(numbers)
