f1 = open('Input/students.txt')
content = f1.read()
f1.close()

names = list(map(str,content.split()))
name_amount = len(names)

f2 = open('Output/output12.txt','w')
f2.write(str(name_amount))
f2.close()