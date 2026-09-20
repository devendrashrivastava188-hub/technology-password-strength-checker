#Technology password strength checker
# I made this project to practice python string handling and conditions.

# I wrote this code to ask the user for a password
password = input("enter a password: ")

# I checked the length of the password
password_length = len(password)

# I checked whether the password contains a number
has_number = any(character.isdigit() for character in password)

# I checked whether the password contains an uppercase letter
has_uppercase = any(character.isupper() for character in password)

print("\n--- password Analysis ---")
print("password Length:",password_length)
print("Contains Number: ",has_number)
print("Contains uppercase Letter:",has_uppercase)

# I checked the password strength
if password_length >= 8 and has_number and has_uppercase:
    strength = "strong"
elif password_length >= 6 and(has_number or has_uppercase):
    strength = "Medium"
else:
    strength = "Weak"
print("Password Strength:",strength)
        
