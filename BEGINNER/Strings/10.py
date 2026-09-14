# Take full name and print initials.
full_name = input("Enter ur fullname:")
words = full_name.split()
intials = ""

for intial in words:
    intials += intial[0].upper() + " "
print(f"Intials: {intials}")