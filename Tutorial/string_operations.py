
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


concatenated = string1 + " " + string2
print(f"\nConcatenated string: {concatenated}")


concatenated2 = " ".join([string1, string2])
print(f"Concatenated using join: {concatenated2}")


print(f"\nOriginal string: {concatenated}")
print(f"Length of string: {len(concatenated)}")


print(f"\nFirst character: {concatenated[0]}")
print(f"Last character: {concatenated[-1]}")


print(f"\nFirst 5 characters: {concatenated[:5]}")
print(f"Last 5 characters: {concatenated[-5:]}")
print(f"Characters from index 2 to 7: {concatenated[2:8]}")
print(f"Every 2nd character: {concatenated[::2]}")

start = int(input("\nEnter start index for substring: "))
end = int(input("Enter end index for substring: "))
print(f"Substring from index {start} to {end}: {concatenated[start:end]}")
