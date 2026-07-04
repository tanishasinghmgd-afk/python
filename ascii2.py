print("ASCII VALUE CHECKER")

print("=" * 40)

char = input("enter a single character: ")

if type(char) is str and len(char) == 1:

    ascii_val = ord(char)

    print(f"\n character: '{char}'")

    print(f"ASCII value: '{ascii_val}'")

    print("\n Character type: ", end="")

if ascii_val >=65 and ascii_val <= 90:
    print("uppercase letter")
elif ascii_val >= 97 and ascii_val <= 122:
    print("lowercase letter")
elif ascii_val >= 48 and ascii_val <= 57:
    print("digit")
elif ascii_val ==32:
    print("space")
else:
    print("special character")                   
    