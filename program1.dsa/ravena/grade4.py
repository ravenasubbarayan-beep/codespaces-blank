# Student Grade Analyzer

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0

for i in range(1, n + 1):
    mark = float(input("Enter mark for subject " + str(i) + ": "))
    total += mark

average = total / n

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

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)