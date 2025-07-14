f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()

big_num = max(map(int, content.split()))

f2 = open('Output/output03.txt', 'w')
f2.write(f'Eng kattasi: {big_num}')
f2.close()
