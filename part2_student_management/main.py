import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "students.txt")


def load_students():
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split("|")
                if len(parts) == 3:
                    roll = parts[0]
                    name = parts[1]
                    marks_str = parts[2].split(",")
                    marks = []
                    for m in marks_str:
                        marks.append(float(m))
                    students.append({
                        "roll": roll,
                        "name": name,
                        "marks": marks
                    })
    except FileNotFoundError:
        # File doesn't exist yet on first run, so return empty list
        pass
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            marks_list = []
            for m in student["marks"]:
                marks_list.append(str(m))
            marks_str = ",".join(marks_list)
            file.write(f"{student['roll']}|{student['name']}|{marks_str}\n")


def find_by_roll(students, roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def add_student(students):
    name = input("Enter student name: ").strip().replace("|", "")
    if name == "":
        print("Name cannot be empty.")
        return

    roll = input("Enter roll number: ").strip().replace("|", "")
    if roll == "":
        print("Roll number cannot be empty.")
        return

    if find_by_roll(students, roll) is not None:
        print("A student with this roll number already exists.")
        return

    try:
        num_subjects = int(input("How many subjects? "))
        if num_subjects <= 0:
            print("Number of subjects must be at least 1.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    marks = []
    for i in range(1, num_subjects + 1):
        while True:
            try:
                m = float(input(f"Enter marks for subject {i} (0-100): "))
                if m < 0 or m > 100:
                    print("Marks must be between 0 and 100.")
                else:
                    marks.append(m)
                    break
            except ValueError:
                print("Invalid input! Please enter a number.")

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n--- All Students ---")
    for student in students:
        print(f"Roll No: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}")


def search_student(students):
    if len(students) == 0:
        print("No student records to search.")
        return

    roll = input("Enter roll number to search: ").strip()
    student = find_by_roll(students, roll)

    if student is not None:
        print("\nStudent Found:")
        print("Name:", student["name"])
        print("Roll No:", student["roll"])
        print("Marks:", student["marks"])
    else:
        print("Student not found.")


def calculate_average(students):
    if len(students) == 0:
        print("No student records found.")
        return

    roll = input("Enter roll number to calculate average: ").strip()
    student = find_by_roll(students, roll)

    if student is not None:
        marks = student["marks"]
        avg = sum(marks) / len(marks)
        print(f"\nStudent: {student['name']} (Roll No: {student['roll']})")
        print("Marks:", marks)
        print("Average Marks:", round(avg, 2))
    else:
        print("Student not found.")


def show_menu():
    print("\n--- Student Management System ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Calculate average marks")
    print("5. Exit")


def main():
    students = load_students()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            calculate_average(students)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 5.")


main()
