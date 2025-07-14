f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()


numbers = list(map(int, content.split()))
sq_pow = list(map(lambda number: number ** 2,numbers))

f2 = open('Output/output07.txt','w')
f2.write(str(sq_pow))
f2.close()