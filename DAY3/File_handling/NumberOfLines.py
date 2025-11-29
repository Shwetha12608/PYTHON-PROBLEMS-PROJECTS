file_name=input("Enter the file name: ")

try:
    with open(file_name,'r',encoding='utf=8',errors='replace') as file:
        Nlines=file.readlines()
        print(f"The number of lines in the file is: {len(Nlines)}")

except FileNotFoundError:
    print(f"The file {file_name} does not exist.")