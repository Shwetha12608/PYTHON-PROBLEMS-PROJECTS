def climb_stairs(n):
    if n ==0 or n==1:
        return 1
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)

# main()
n=4
result= climb_stairs(n)#Calling in main
print(result)

