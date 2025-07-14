f1 = open('Input/students.txt')
content = f1.read()
f1.close()

names = list(map(str,content.split()))
user_search = input('Ism kiriting: ')


if user_search in names:
    result = user_search
else:
    result = "No'malum ism"    


    


f2 = open('Output/output18.txt','w')
f2.write(str(result))
f2.close()
