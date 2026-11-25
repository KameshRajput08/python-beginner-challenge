names = ["Aman", "Priya", "Rohan", "Sneha", "Karan"]

search_name = input("Enter a name to search: ")

found = False
for name in names:
    if name.lower() == search_name.lower():
        found = True
        break

if found:
    print(search_name, "was found in the list.")
else:
    print(search_name, "was not found in the list.")
