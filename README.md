# Python Beginner Challenge (Task 2)

This repository contains my solutions for the **Python Beginner Challenge** assignment, including the Part 1 fundamental exercises and the Part 2 **Student Management System** mini-project.

## Folder Structure

- `part1/` - Practice scripts organized by topic:
  - `01_basics/` - `hello.py`, student variables, basic arithmetic
  - `02_data_types_operators/` - data types, Celsius to Fahrenheit, rectangle area/perimeter, operators
  - `03_conditionals/` - even/odd, grade calculator, leap year, simple calculator
  - `04_loops/` - 1 to 100, multiplication table, sum 1 to N, vowel counter, prime numbers
  - `05_strings_lists_dicts/` - lists, marks stats, dictionary, name search, character count
  - `06_functions/` - largest of three, prime check, average marks, calculator with functions
  - `07_file_error_handling/` - file read/write, saving student marks, `try-except` input handling, missing/empty file check
- `part2_student_management/` - Menu-driven Student Management System (`main.py`)
- `screenshots/` - Screenshots of the program running

## How to Run

Make sure Python 3 is installed.

Run any Part 1 script from the project folder, for example:

```bash
python3 part1/01_basics/hello.py
```

To run the Student Management System:

```bash
python3 part2_student_management/main.py
```

Follow the menu options (1 to 5):
1. Add student
2. View all students
3. Search student by roll number
4. Calculate average marks
5. Exit

## Python Concepts Used

- **Variables & Data Types:** Used strings, integers, floats, lists, and dictionaries to store student names, roll numbers, and marks.
- **Conditionals & Loops:** Used `if-elif-else` for menu choices and validation, and `while` / `for` loops to keep the menu running and process records.
- **Functions:** Broke the Student Management System into small functions (`load_students`, `save_students`, `add_student`, `view_students`, `search_student`, `calculate_average`) to keep the code clean and organized.
- **File Handling:** Stored student records in `students.txt` using `open()` so data stays saved even after closing the program.
- **Error Handling:** Used `try-except` blocks (`ValueError`, `FileNotFoundError`) so invalid inputs or a missing data file don't crash the program.

## Screenshots

*(Add your screenshots here after saving them in the `screenshots/` folder, for example:)*

- `screenshots/01_add_student.png`
- `screenshots/02_view_students.png`
- `screenshots/03_search_student.png`
