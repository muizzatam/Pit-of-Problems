grades = {"A+": 5.0, "A": 4.5, "A-": 4.0, "B": 3.5, "B-": 3.0, "C": 2.5, "D": 2.0}

done = False
points = 0
num = 0

while not done:
    grade = input("")
    if grade in grades:
        num += 1
        points += grades[grade]
    elif not grade:
        done = True
    else:
        print("Invalid Grade")

print(points / num)
