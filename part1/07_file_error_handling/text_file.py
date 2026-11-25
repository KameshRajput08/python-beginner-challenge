filename = "sample.txt"

# Writing text to a file
with open(filename, "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("I am learning file handling in Python.\n")

print("Data written to", filename)

# Reading text back from the file
with open(filename, "r") as file:
    content = file.read()

print("\nFile content:")
print(content)
