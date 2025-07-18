f1 = open('Input/grades.csv')
lines = f1.readlines()
f1.close()

grades = []
for line in lines[1:]:
    name, grade = line.strip().split(",")
    grades.append(int(grade))

avg = sum(grades) / len(grades)

f2 = open('Output/output20.txt', "w")
f2.write(f'average grade is - {avg}')
f2.close()
