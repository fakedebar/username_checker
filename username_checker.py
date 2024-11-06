username = str(input("Enter your username: "))
length = len(username)
digit = any(char.isdigit() for char in username)
spaces = " " in username
if length >=12:
    print("Your username more than 12 characters!")
elif digit:
    print("Your username contain digits!")
elif spaces:
    print("Your username contain spaces!")
else:
    print("Your username registerd successfully!")


