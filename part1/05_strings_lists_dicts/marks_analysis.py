marks = []

for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nResults:")
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
