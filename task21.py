f1 = open('Input/grades.csv')
content = f1.readlines()
f1.close()
students = []
for line in content[1:]:
    name , grade = line.strip().split(",")
    students.append((name, int(grade)))

max_grade = 0
for student in students:
    if student[1] > max_grade:
        max_grade = student[1]

students_5 = []
for student in students:
    if student[1] == max_grade:
        students_5.append(student[0])

f2 = open('Output/output21.txt', 'w')
f2.write(f"Eng yuqori ball - {max_grade}\n")
f2.write("Bu ballni olganlar:\n")
for name in students_5:
    f2.write(f"- {name}\n")
f2.close()