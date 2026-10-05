# Student Grade Analyzer with Subject Grades

n = int(input("Enter number of subjects: "))
total = 0

for i in range(1, n + 1):
    mark = float(input("Enter mark for subject " + str(i) + ": "))
    total += mark

    if mark >= 90:
        print("Subject", i, ": A+")
    elif mark >= 80:
        print("Subject", i, ": A")
    elif mark >= 70:
        print("Subject", i, ": B")
    elif mark >= 60:
        print("Subject", i, ": C")
    elif mark >= 50:
        print("Subject", i, ": D")
    else:
        print("Subject", i, ": F")

average = total / n

if average >= 90:
    final_grade = "A+"
elif average >= 80:
    final_grade = "A"
elif average >= 70:
    final_grade = "B"
elif average >= 60:
    final_grade = "C"
elif average >= 50:
    final_grade = "D"
else:
    final_grade = "F"

print("\nTotal Marks =", total)
print("Average Marks =", average)
print("Final Grade =", final_grade)