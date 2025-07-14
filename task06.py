f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()

numbers = list(map(int, content.split()))
odd_numbers = list(filter(lambda n: n % 2 == 1, numbers))

f2 = open('odd_numbers.txt',"x")
f2.write(str(odd_numbers))
f2.close()