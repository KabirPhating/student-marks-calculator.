
name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

print("Student Name:", name)

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")
