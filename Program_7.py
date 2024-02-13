is_palindrome = lambda s: s == s[::-1]


string_list = ["level", "hello", "radar", "python", "madam", "racecar"]
palindromes = list(filter(is_palindrome, string_list))

print("Palindromes in the list:")
print(palindromes)