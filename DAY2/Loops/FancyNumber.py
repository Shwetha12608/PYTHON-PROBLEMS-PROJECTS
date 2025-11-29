num=input("Enter the 5 digit number")

if len(num)!=4 or not num.isdigit():
    print("Invalid")

else:
    digits=[int(i) for i in num] #Converting to int
    
    increasing=all(
        digits[i]+1==digits[i+1]
        for i in range(3)
    )
    decreasing=all(
        digits[i]-1==digits[i+1]
        for i in range(3)
    )
    if increasing==True:
        print("Increasing fancy number")
    elif decreasing==True:
        print("Decreasing Fancy number")
    else:
        print("Not fancy number")