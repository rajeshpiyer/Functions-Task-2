check = lambda string, character: string.startswith(character)

# Test the lambda function
sentence = input("Enter a Sentence : ")
check_character = input("Enter a character to check")

if check(sentence,check_character):
    print(f"The string '{sentence}' starts with the character '{check_character}'.")
else:
    print(f"The string '{sentence}' does not start with the character '{check_character}'.")