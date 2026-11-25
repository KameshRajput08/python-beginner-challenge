filename = input("Enter file name to read (e.g. data.txt): ")

try:
    with open(filename, "r") as file:
        content = file.read().strip()
        if content == "":
            print("The file is empty.")
        else:
            print("File content:")
            print(content)
except FileNotFoundError:
    print("Error: File not found.")
