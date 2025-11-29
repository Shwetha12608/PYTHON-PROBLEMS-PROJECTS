password=input("Enter the password: ")

if len(password)<6:
    print("Invalid")
else:
    fifth_char=password[4]

    if not (fifth_char.isdigit() and 1<=int(fifth_char)<=5):
        print("Invalid")
    else:
        if any(char.isspace() for char in password):
            print("Invalid")
        else:
            print("valid")