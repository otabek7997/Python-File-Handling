f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()

numbers = list(map(int, content.split()))
five = list(filter(lambda n: n % 5 == 0, numbers))


f2 = open('Output/output08.txt', 'w')
f2.write(str(five))
f2.close()