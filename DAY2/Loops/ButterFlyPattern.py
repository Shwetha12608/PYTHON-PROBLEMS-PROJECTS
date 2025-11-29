n=4
for i in range(1,n+1):
    # Left
    for j in range(1,i+1):
        print("*",end="")
    
    # Spaces
    for j in range(1,2*(n-i)+1):
        print(" ",end="")
# Right 
    for j in range(1,i+1):
        print("*",end="")    
    print()

# LOWER PART


for i in range(n,0,-1):
    # Left
    for j in range(1,i+1):
        print("*",end="")
    
    # Spaces
    for j in range(1,2*(n-i)+1):
        print(" ",end="")
# Right 
    for j in range(1,i+1):
        print("*",end="")
    print()
