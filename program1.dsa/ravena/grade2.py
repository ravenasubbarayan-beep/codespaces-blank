# Student Grade Analyzer using List

marks = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input("Enter mark for subject " + str(i + 1) + ": "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\nMarks =", marks)
print("Total =", total)
print("Average =", average)
print("Grade =", grade)