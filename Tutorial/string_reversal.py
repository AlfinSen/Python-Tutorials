def reverse_using_slicing(text):
    return text[::-1]


def reverse_using_loop(text):
    reversed_str = ""
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str


def reverse_using_reversed(text):
    return "".join(reversed(text))


def reverse_using_recursion(text):
    if len(text) == 0:
        return text
    else:
        return reverse_using_recursion(text[1:]) + text[0]

string = input("Enter a string to reverse: ")

print("\nOriginal string:", string)
print("\nReversed strings using different methods:")
print(f"1. Using slicing: {reverse_using_slicing(string)}")
print(f"2. Using loop: {reverse_using_loop(string)}")
print(f"3. Using reversed(): {reverse_using_reversed(string)}")
print(f"4. Using recursion: {reverse_using_recursion(string)}")
