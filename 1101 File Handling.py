# Task 2
# with open("newfile.txt","w") as writefile:
#     writefile.write("Bennet Thomas,")
#     writefile.write(" Black,")
#     writefile.write(" October")

#Task 3
# items = []
# names = []
# marks = []
# with open("pupils.txt") as readfile:
#     line = readfile.readline().rstrip('\n')
#     while line:
#         items = line.split(",")
#         names.append(items[0])
#         marks.append(items[1])
#         line = readfile.readline().rstrip('\n')

# for index in range(len(names)):
#     print(names[index], '-', marks[index])

#Task 4

names = ["John","Joan","Mark","Michael"]
birthMonth = ['January', 'February', 'March', 'April']
ages = [23,35,23,8]

with open("names.txt","w") as wfile:
    for counter in range(0,len(names)):
        wfile.write(names[counter] + "," + str(ages[counter])+"\n")


