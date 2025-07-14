f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()


numbers = list(map(int, content.split()))
total = sum(numbers)
avg = total/len(numbers)

f2 = open('Output/output05.txt','w')
f2.write(f'Average: {avg}')
f2.close()