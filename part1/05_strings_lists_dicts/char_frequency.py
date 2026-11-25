text = input("Enter a string: ")

counts = {}
for ch in text:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1

print("Character counts:")
for ch in counts:
    print(f"'{ch}': {counts[ch]}")
