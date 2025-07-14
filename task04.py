f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()

numbers = list(map(int, content.split()))
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))


f2 = open('Output/output04.txt', 'w')
f2.write(str(even_numbers))
f2.close()
