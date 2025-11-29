name=input("Enter the sentence: ")

mid=len(name)//2


# result=name[::-1]

first_half=name[:mid]
Second_half=name[mid:]

result=first_half[::-1]+Second_half[::-1]
print(result)

