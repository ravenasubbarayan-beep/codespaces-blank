# Student Grade Analyzer using While Loop

n = int(input("Enter number of subjects: "))

i = 1
total = 0

while i <= n:
    mark = float(input("Enter mark for subject " + str(i) + ": "))
    total = total + mark
    i = i + 1

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

print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Final Grade:", grade)