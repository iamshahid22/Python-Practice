# Check whether a string is a palindrome.
word = input("Enter a word:")
palindrome = word[::-1]

if word==palindrome:
    print("Word is palindrome..")
else:
    print("Not a palindrome..")