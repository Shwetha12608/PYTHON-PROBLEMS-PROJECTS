password=input("Enter the password: ")


Encryption=password.replace('1','2')\
                    .replace('A','B')\
                    .replace('a','@')
password=Encryption

print("Encrypted password",password)