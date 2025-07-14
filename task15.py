
f1 = open('Input/students.txt')
content = f1.read()
f1.close()


names = content.split()
result = map(lambda name: name + " - " + str(len(name)) + " harf", names)


f2 = open('Output/output15.txt', 'w')
f2.write('\n'.join(result))
f2.close()
