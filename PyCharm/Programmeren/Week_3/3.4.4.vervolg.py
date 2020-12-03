numbers = (83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0)

for number in numbers:
    if number >=75:
        grade = "First"
    elif number >=70:
        grade = "Upper second"
    elif number >=60:
        grade = "Second"
    elif number >=50:
        grade = "Third"
    elif number >=45:
        grade = "F1 Supp"
    elif number >=40:
        grade = "F2"
    elif number <40:
        grade = "F3"

print (number, grade)



