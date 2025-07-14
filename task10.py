f1 = open('Input/numbers.txt')
content = f1.read()
f1.close()


numbers = list(map(int, content.split()))
sorted_ones = sorted(numbers, key=lambda number:number)


f2 = open('Output/output10.txt','w')
f2.write(str(sorted_ones))
f2.close()