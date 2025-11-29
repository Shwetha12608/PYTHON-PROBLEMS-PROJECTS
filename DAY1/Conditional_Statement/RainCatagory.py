rainSize=int(input("Enter the rain size (in mm): "))

# Int(),Float(),Str(),Bool()

if rainSize<1 and rainSize>=0:
    print("No Rain")
elif rainSize>=1 and rainSize<5:
    print("Light Rain")
elif rainSize>=5 and rainSize<10:
    print("Moderate Rain")
elif rainSize>=10:
    print("Heavy Rain")
else:
    print ("Invalid Input")
