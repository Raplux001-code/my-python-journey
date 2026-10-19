# Grade Calculator by Raplux001-code
name = input("Enter student name: ")
score = int(input("Enter score (0-100): "))

if score >= 70:
    grade = "A - Excellent"
elif score >= 60:
    grade = "B - Very Good"
elif score >= 50:
    grade = "C - Good"
elif score >= 45:
    grade = "D - Pass"
else:
    grade = "F - Fail"

print(f"{name} scored {score} - Grade: {grade}")