f1 = open('Input/students.txt')
content = f1.read()
f1.close()

names = list(map(str,content.split()))

f2 = open('Output/output11.txt','w')
f2.write(str(names))
f2.close()
