# *agrs

def add(inp_type,*args):
    if inp_type=="str":
        result=" ".join(str(x) for x in args)
    
    elif inp_type=="int":
        result=sum(int(x) for x in args)
    
    else:
        result="Invalid Input Type"

    print(result)


# MAIN()
input_type=input("Enter the input type (str/int): ").strip()
inp1=10
inp2=20
# add(input_type,inp1,inp2)
# add(input_type,10,20,30,40,50)
add(input_type,"BAVITH","SHETTY")
