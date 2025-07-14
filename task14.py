f1 = open('Input/students.txt')
content = f1.read()
f1.close()

names = list(map(str,content.split()))
sorted_ones = sorted(names, key=lambda name:name , reverse = True)


f2 = open('Output/output14.txt','w')
f2.write(str(sorted_ones))
f2.close()