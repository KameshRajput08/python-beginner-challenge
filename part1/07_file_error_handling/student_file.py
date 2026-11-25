filename = "student_marks.txt"

name = input("Enter student name: ")
marks = input("Enter marks: ")

with open(filename, "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Marks: {marks}\n")

print("\nSaved data from file:")
with open(filename, "r") as file:
    print(file.read())
