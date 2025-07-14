f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()

total = sum(map(int,content.split()))

f2 = open('Output/output02.txt','w')
f2.write(f'total: {total}')
f2.close()