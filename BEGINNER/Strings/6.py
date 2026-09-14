# Count vowels in a string.
word = input("Enter word:")
vowels = "aeiouAEIOU"
count = 0
for letter in word:
    if letter in vowels:
        count+=1
print(f"Total vowels: {count}")