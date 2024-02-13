check = lambda s: s.isdigit()

input_string = "9207413"
if check(input_string):
    print(f"The string '{input_string}' is a number.")
else:
    print(f"The string '{input_string}' is not a number.")
