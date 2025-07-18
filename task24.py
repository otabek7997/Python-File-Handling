f1 = open('Input/grades.csv')
lines = f1.readlines()
f1.close()

grades = []
for line in lines[1:]:
    name, grade = line.strip().split(",")
    grades.append(int(grade))

avg = sum(grades) / len(grades)

better_then_avg =[]
for line in lines[1:]:
    name , grade = line.strip().split(',')
    if int(grade) > avg:
        better_then_avg.append(name) 

f2 = open('Output/output24.txt', "w")
f2.write(f"O'rtachadan baland olganlar")
for name in better_then_avg:
    f2.write(f' - {name}')
f2.close()
