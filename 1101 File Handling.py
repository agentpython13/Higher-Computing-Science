# Task 2
# with open("newfile.txt","w") as writefile:
#     writefile.write("Bennet Thomas,")
#     writefile.write(" Black,")
#     writefile.write(" October")

#Task 3
items = []
names = []
marks = []
with open("pupils.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        names.append(items[0])
        marks.append(items[1])
        line = readfile.readline().rstrip('\n')

for index in range(len(names)):
    print(names[index], '-', marks[index])


