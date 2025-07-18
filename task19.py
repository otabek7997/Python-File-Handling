with open("Input/grades.csv") as f1, open("Output/output19.txt","w") as f2:
    for line in f1:
        name , grade = line.strip().split(",")
        f2.write(f"{name} - {grade}\n")