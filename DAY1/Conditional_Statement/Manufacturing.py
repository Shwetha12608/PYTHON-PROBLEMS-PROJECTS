# SOLVING ARITHMATIC EXPRESSION

# GIVEN DATA
# V=200,W=540

# V=TW+FW....(1)
# W=(FW*4)+(TW*2)....(2)

# W=2(TW+2FW)
# W/2=TW+2FW

# V=TW+FW
# SOLVING THE EQN For Finding FW

# APPLY THIS
# FW=(W/2)-V
# TW=V-FW

V=200
W=540

if(V>=W or W<2 or W%2!=0):
    print("Invalid Input")

else:
    FW=(W/2)-V
    TW=V-FW

    print("The number of Two wheeler: ",TW)
    print("The number of Four Wheeler: ",FW)




