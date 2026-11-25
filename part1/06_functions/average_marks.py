def calculate_average(marks_list):
    if len(marks_list) == 0:
        return 0
    return sum(marks_list) / len(marks_list)


marks = [76, 84, 91, 68, 88]
avg = calculate_average(marks)

print("Marks:", marks)
print("Average:", avg)
